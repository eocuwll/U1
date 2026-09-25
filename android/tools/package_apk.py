#!/usr/bin/env python3
"""Assemble un APK non signé sans le SDK Android (aapt indisponible) :
AndroidManifest.xml binaire (AXML), resources.arsc minimal (une icône),
classes.dex, assets/www/… ; entrées non compressées alignées sur 4 octets.

Usage : package_apk.py classes.dex www_dir icon.png out.apk version_code version_name
"""
import struct, sys, zipfile, pathlib

PKG = 'ma.normes.nmen'
LABEL = 'Normes NM-EN'
ICON_ID = 0x7f010000  # drawable/icon

# ---------- pool de chaînes (UTF-16) ----------
def string_pool(strings):
    offs, data = [], b''
    for s in strings:
        offs.append(len(data))
        enc = s.encode('utf-16-le')
        data += struct.pack('<H', len(s)) + enc + b'\0\0'
    while len(data) % 4: data += b'\0'
    header = 28
    start = header + 4 * len(strings)
    body = b''.join(struct.pack('<I', o) for o in offs) + data
    return struct.pack('<HHIIIIII', 0x0001, header, header + len(body), len(strings), 0, 0, start, 0) + body

# ---------- AndroidManifest.xml binaire ----------
ATTR = {  # nom -> id de ressource android
    'label': 0x01010001, 'icon': 0x01010002, 'name': 0x01010003, 'exported': 0x01010010,
    'configChanges': 0x0101001f, 'minSdkVersion': 0x0101020c, 'versionCode': 0x0101021b,
    'versionName': 0x0101021c, 'targetSdkVersion': 0x01010270, 'allowBackup': 0x01010280,
    'hardwareAccelerated': 0x010102d3,
}
ANDROID_NS = 'http://schemas.android.com/apk/res/android'
T_REF, T_STR, T_DEC, T_HEX, T_BOOL = 0x01, 0x03, 0x10, 0x11, 0x12

def manifest(vcode, vname):
    # (tag, [(ns?, attr, type, value)], children)
    tree = ('manifest', [(False, 'package', T_STR, PKG), (True, 'versionCode', T_DEC, vcode), (True, 'versionName', T_STR, vname)], [
        ('uses-sdk', [(True, 'minSdkVersion', T_DEC, 24), (True, 'targetSdkVersion', T_DEC, 34)], []),
        ('application', [(True, 'label', T_STR, LABEL), (True, 'icon', T_REF, ICON_ID),
                         (True, 'allowBackup', T_BOOL, True), (True, 'hardwareAccelerated', T_BOOL, True)], [
            ('activity', [(True, 'name', T_STR, PKG + '.MainActivity'), (True, 'exported', T_BOOL, True),
                          (True, 'configChanges', T_HEX, 0x04A0)], [
                ('intent-filter', [], [
                    ('action', [(True, 'name', T_STR, 'android.intent.action.MAIN')], []),
                    ('category', [(True, 'name', T_STR, 'android.intent.category.LAUNCHER')], []),
                ]),
            ]),
        ]),
    ])
    attr_names = [a for a in ATTR]  # chaînes d'attributs android en tête du pool
    strings = list(attr_names)
    def idx(s):
        if s not in strings: strings.append(s)
        return strings.index(s)
    for s in ['android', ANDROID_NS]: idx(s)
    def collect(node):
        tag, attrs, kids = node
        idx(tag)
        for ns, n, t, v in attrs:
            idx(n)
            if t == T_STR: idx(v)
        for k in kids: collect(k)
    collect(tree)
    NS = strings.index(ANDROID_NS)
    chunks = []
    chunks.append(struct.pack('<HHIIIII', 0x0100, 16, 24, 1, 0xFFFFFFFF, strings.index('android'), NS))
    def emit(node, line=[2]):
        tag, attrs, kids = node
        enc = []
        for ns, n, t, v in sorted(attrs, key=lambda a: ATTR.get(a[1], 0xFFFFFFFF) if a[0] else -1):
            raw = strings.index(v) if t == T_STR else 0xFFFFFFFF
            data = strings.index(v) if t == T_STR else (0xFFFFFFFF if (t == T_BOOL and v) else int(v))
            enc.append(struct.pack('<IIIHBBI', NS if ns else 0xFFFFFFFF, strings.index(n), raw, 8, 0, t, data))
        body = struct.pack('<IIHHHHHH', 0xFFFFFFFF, strings.index(tag), 20, 20, len(enc), 0, 0, 0) + b''.join(enc)
        chunks.append(struct.pack('<HHIII', 0x0102, 16, 16 + len(body), line[0], 0xFFFFFFFF) + body)
        line[0] += 1
        for k in kids: emit(k)
        chunks.append(struct.pack('<HHIIIII', 0x0103, 16, 24, line[0], 0xFFFFFFFF, 0xFFFFFFFF, strings.index(tag)))
    emit(tree)
    chunks.append(struct.pack('<HHIIIII', 0x0101, 16, 24, 99, 0xFFFFFFFF, strings.index('android'), NS))
    pool = string_pool(strings)
    resmap_body = b''.join(struct.pack('<I', ATTR[a]) for a in attr_names)
    resmap = struct.pack('<HHI', 0x0180, 8, 8 + len(resmap_body)) + resmap_body
    body = pool + resmap + b''.join(chunks)
    return struct.pack('<HHI', 0x0003, 8, 8 + len(body)) + body

# ---------- resources.arsc : une ressource drawable/icon ----------
def resources():
    values = string_pool(['res/drawable/icon.png'])
    types = string_pool(['drawable'])
    keys = string_pool(['icon'])
    spec = struct.pack('<HHIBBHI', 0x0202, 16, 16 + 4, 1, 0, 0, 1) + struct.pack('<I', 0)
    config = struct.pack('<I', 64) + b'\0' * 60
    type_hdr = 20 + len(config)
    entries = struct.pack('<I', 0) + struct.pack('<HHI', 8, 0, 0) + struct.pack('<HBBI', 8, 0, T_STR, 0)
    typ = struct.pack('<HHIBBHII', 0x0201, type_hdr, type_hdr + len(entries), 1, 0, 0, 1, type_hdr + 4) + config + entries
    name = PKG.encode('utf-16-le').ljust(256, b'\0')
    pkg_hdr = 288
    type_off = pkg_hdr
    key_off = pkg_hdr + len(types)
    pkg_body = types + keys + spec + typ
    pkg = struct.pack('<HHII', 0x0200, pkg_hdr, pkg_hdr + len(pkg_body), 0x7f) + name + \
          struct.pack('<IIIII', type_off, 1, key_off, 1, 0) + pkg_body
    body = values + pkg
    return struct.pack('<HHII', 0x0002, 12, 12 + len(body), 1) + body

# ---------- zip aligné ----------
def add(z, name, data, store):
    info = zipfile.ZipInfo(name, date_time=(2026, 9, 25, 0, 0, 0))
    info.compress_type = zipfile.ZIP_STORED if store else zipfile.ZIP_DEFLATED
    if store:
        off = z.fp.tell() + 30 + len(name.encode())
        info.extra = b'\0' * ((4 - off % 4) % 4)
    z.writestr(info, data)

def main():
    dex, www, icon, out, vcode, vname = sys.argv[1:7]
    with zipfile.ZipFile(out, 'w') as z:
        add(z, 'AndroidManifest.xml', manifest(int(vcode), vname), False)
        add(z, 'resources.arsc', resources(), True)
        add(z, 'classes.dex', open(dex, 'rb').read(), False)
        add(z, 'res/drawable/icon.png', open(icon, 'rb').read(), True)
        root = pathlib.Path(www)
        for p in sorted(root.rglob('*')):
            if p.is_file():
                add(z, 'assets/www/' + p.relative_to(root).as_posix(), p.read_bytes(), False)
    print('APK non signé :', out)

if __name__ == '__main__':
    main()
