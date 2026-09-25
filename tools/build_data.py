#!/usr/bin/env python3
"""Construit app/data/normes.js à partir de data/imanor_nm_2023.json.

Pour chaque norme NM :
  eu  : référence européenne / internationale
  fr  : référence française (NF, NF EN, NF DTU…)
  s   : statut de l'équivalence
        imanor  = équivalence déclarée dans le guide IMANOR
        auto    = déduite : une EN est reprise en France sous « NF EN » (même numéro)
        verif   = reprise française probable, à vérifier (ISO / IEC / CEN-TS)
        titre   = NM nationale dont l'intitulé est identique à un texte français
        fonc    = équivalent fonctionnel (même produit/ouvrage), pas une reprise
        aucune  = pas d'équivalence connue dans cette base
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = json.load(open(ROOT / 'data/imanor_nm_2023.json', encoding='utf-8'))

LOTS = {
    '4.1': 'Matériels et installations électriques',
    '4.1.1': 'Produits électriques',
    '4.1.2': 'Fils, câbles et accessoires',
    '4.1.3': 'Installations électriques',
    '4.2': 'Assainissement et adduction d’eau potable',
    '4.3': 'Matériaux de construction',
    '4.3.1': 'Produits de fonderie',
    '4.3.2': 'Fer à béton et câbles de précontrainte',
    '4.3.3': 'Liants hydrauliques',
    '4.3.4': 'Produits en terre cuite',
    '4.3.5': 'Produits de carrière',
    '4.4': 'Gros œuvre',
    '4.4.1': 'Bétons, mortiers et produits dérivés',
    '4.4.2': 'Couverture et étanchéité',
    '4.4.3': 'Chaudronnerie et menuiserie métalliques',
    '4.5': 'Second œuvre',
    '4.5.1': 'Plomberie',
    '4.5.2': 'Isolation thermique',
    '4.5.3': 'Bois, liège et produits dérivés',
    '4.5.4': 'Menuiserie des portes et fenêtres',
    '4.5.5': 'Robinetterie et produits sanitaires',
    '4.5.6': 'Vitrage et miroiterie',
    '4.5.7': 'Quincaillerie',
    '4.5.8': 'Carreaux de revêtement',
    '4.5.9': 'Peintures et vernis',
    '4.5.10': 'Acoustique',
    '4.6': 'Développement durable & performance des bâtiments',
    '4.7': 'Travaux routiers',
    '4.7.1': 'Chaussées et liants hydrocarbonés',
    '4.7.2': 'Signalisation routière',
    '4.8': 'Terrassement',
    '4.8.1': 'Produits géotechniques',
    '4.8.2': 'Travaux géotechniques',
    '4.9': 'Énergies renouvelables',
    '4.10': 'Sécurité incendie',
    '4.11': 'Produits chimiques – traitement de l’eau potable',
}

# Correspondances pour des NM nationales sans équivalence dans le guide IMANOR.
# (fr, eu, statut, note)
CURATED = {
    # Intitulé identique à un texte français
    'NM 10.1.184': ('NF DTU 21 (NF P 18-201)', 'EN 13670', 'titre', 'Même intitulé que le NF DTU 21 ; le DTU renvoie à la NF EN 13670/CN et à la NF EN 206/CN.'),
    'NM 10.8.913': ('DTU 43.1 (NF P 84-204)', '', 'titre', 'Même intitulé que le DTU 43.1.'),
    'NM 10.2.483': ('NF DTU 36.5 P1-1', '', 'titre', 'Même intitulé que le NF DTU 36.5.'),
    'NM 03.3.142': ('NF DTU 59.1 P1-1 (NF P 74-202)', '', 'titre', 'Même intitulé que le NF DTU 59.1 (CCT).'),
    'NM 03.3.143': ('NF DTU 59.1 P1-2', '', 'titre', 'Même intitulé que le NF DTU 59.1 (CGM).'),
    'NM 03.3.144': ('NF DTU 59.1 P2', '', 'titre', 'Même intitulé que le NF DTU 59.1 (CCS).'),
    'NM 03.3.145': ('NF DTU 42.1 P1-1', '', 'titre', 'Même intitulé que le NF DTU 42.1 (CCT).'),
    'NM 03.3.146': ('NF DTU 42.1 P1-2', '', 'titre', 'Même intitulé que le NF DTU 42.1 (CGM).'),
    'NM 03.3.147': ('NF DTU 42.1 P2', '', 'titre', 'Même intitulé que le NF DTU 42.1 (CCS).'),
    'NM 10.8.808': ('NF P 03-001', '', 'titre', 'CCAG marchés privés – bâtiment.'),
    'NM 10.8.809': ('NF P 03-002', '', 'titre', 'CCAG marchés privés – génie civil.'),
    'NM 13.1.219': ('NF P 98-086', '', 'titre', 'Dimensionnement structurel des chaussées routières – chaussées neuves.'),
    'NM 13.1.220': ('NF P 98-331', '', 'titre', 'Tranchées : ouverture, remblayage, réfection.'),
    'NM 13.1.279': ('NF P 98-335', '', 'titre', 'Mise en œuvre des pavés et dalles en béton / terre cuite / pierre.'),
    'NM 13.1.174': ('NF P 94-325-1', '', 'titre', 'Ouvrages en gabions.'),
    'NM 13.1.175': ('NF P 94-325-2', '', 'titre', 'Ouvrages en gabions.'),
    'NM 13.1.125': ('NF P 94-105', '', 'titre', 'Contrôle du compactage au pénétromètre.'),
    'NM 13.1.126': ('NF P 94-102-1', '', 'titre', 'Sol traité au liant hydraulique.'),
    'NM 10.1.301': ('NF P 95-101', 'EN 1504 (série)', 'titre', 'Réparation des ouvrages : reprise du béton dégradé superficiellement.'),
    # Équivalents fonctionnels (même produit, textes différents)
    'NM 10.1.008': ('NF EN 206+A2/CN', 'EN 206 (ex EN 206-1)', 'auto', 'IMANOR cite l’EN 206-1 (A1, A2). En France : NF EN 206+A2/CN (P 18-325).'),
    'NM 10.1.004': ('NF EN 197-1', 'EN 197-1', 'fonc', 'Ciments courants. La NM 10.1.004 a ses propres classes : comparer avant substitution.'),
    'NM 01.4.096': ('NF A 35-080-1', 'EN 10080', 'fonc', 'Barres HA B500 (France : marque NF-AFCAB).'),
    'NM 01.4.097': ('NF A 35-080-1', 'EN 10080', 'fonc', 'Barres HA B500 (France : marque NF-AFCAB).'),
    'NM 01.4.095': ('NF A 35-080-1', 'EN 10080', 'fonc', 'Aciers pour béton armé.'),
    'NM 01.4.220': ('NF A 35-080-2', 'EN 10080', 'fonc', 'Treillis soudés.'),
    'NM 10.1.009': ('NF EN 771-3 (+ NF EN 771-3/CN)', 'EN 771-3', 'fonc', 'Blocs (agglos) en béton de granulats.'),
    'NM 10.1.042': ('NF EN 771-1 (+ NF EN 771-1/CN)', 'EN 771-1', 'fonc', 'Briques en terre cuite.'),
    'NM 10.6.700': ('NF EN 771-1 (+ NF EN 771-1/CN)', 'EN 771-1', 'fonc', 'Briques et blocs en terre cuite.'),
    'NM 10.6.702': ('NF EN 771-1', 'EN 771-1', 'fonc', 'Briques apparentes.'),
    'NM 10.6.703': ('NF EN 771-1', 'EN 771-1', 'fonc', 'Blocs apparents.'),
    'NM 10.6.300': ('NF EN 1304', 'EN 1304', 'fonc', 'Tuiles de terre cuite.'),
    'NM 10.6.301': ('NF EN 1304', 'EN 1304', 'fonc', 'Tuiles de terre cuite.'),
    'NM 10.6.302': ('NF EN 1304', 'EN 1304', 'fonc', 'Tuiles de terre cuite.'),
    'NM 10.6.706': ('NF EN 1344', 'EN 1344', 'fonc', 'Pavés en terre cuite.'),
    'NM 10.1.165': ('NF EN 12620', 'EN 12620', 'fonc', 'Granulats pour béton.'),
    'NM 10.1.014': ('NF EN 1342 / NF EN 1343', 'EN 1342 / EN 1343', 'fonc', 'Pavés et bordures en pierre naturelle.'),
    'NM 10.6.159': ('NF EN 14411', 'EN 14411 / ISO 13006', 'fonc', 'Carreaux céramiques groupe BIII.'),
    'NM 10.6.176': ('NF EN 14411', 'EN 14411 / ISO 13006', 'fonc', 'Carreaux céramiques groupe BI.'),
    'NM 10.6.177': ('NF EN 14411', 'EN 14411 / ISO 13006', 'fonc', 'Carreaux céramiques groupe BIIa.'),
    'NM 10.6.178': ('NF EN 14411', 'EN 14411 / ISO 13006', 'fonc', 'Carreaux céramiques groupe BIIb.'),
    'NM 10.7.014': ('NF EN 12150-1', 'EN 12150-1', 'fonc', 'Verre trempé.'),
    'NM 10.7.013': ('NF EN ISO 12543 (série)', 'EN ISO 12543', 'fonc', 'Verre feuilleté.'),
    'NM 10.7.012': ('NF EN 572-2', 'EN 572-2', 'fonc', 'Glace (verre float).'),
    'NM 10.7.011': ('NF EN 572-4', 'EN 572-4', 'fonc', 'Verre étiré.'),
    'NM 10.4.056': ('NF EN 997', 'EN 997', 'fonc', 'Cuvettes de WC.'),
    'NM 10.4.054': ('NF EN 14688', 'EN 14688', 'fonc', 'Lavabos.'),
    'NM 10.4.005': ('NF EN 817', 'EN 817', 'fonc', 'Mitigeurs mécaniques.'),
    'NM 10.4.002': ('NF EN 200', 'EN 200', 'fonc', 'Robinets simples et mélangeurs.'),
    'NM 01.4.047': ('NF EN 545', 'EN 545', 'fonc', 'Fonte ductile – conduites d’eau sous pression.'),
    'NM 10.9.003': ('NF EN 1917 (+ NF P 16-346-2)', 'EN 1917', 'fonc', 'Regards de visite en béton.'),
    'NM 10.4.263': ('NF EN 124 (série)', 'EN 124', 'fonc', 'Dispositifs de couronnement et de fermeture.'),
    'NM 10.4.264': ('NF EN 124 (série)', 'EN 124', 'fonc', 'Dispositifs de couronnement et de fermeture.'),
    'NM 03.4.002': ('NF EN 12591', 'EN 12591', 'fonc', 'Bitumes routiers.'),
    'NM 03.4.079': ('NF EN 15322', 'EN 15322', 'fonc', 'Liants bitumineux fluxés et fluidifiés.'),
    'NM 03.4.003': ('NF EN 15322', 'EN 15322', 'fonc', 'Liants bitumineux fluxés et fluidifiés.'),
    'NM 13.1.207': ('NF EN 13108-7', 'EN 13108-7', 'fonc', 'Bétons bitumineux drainants.'),
    'NM 14.5.002': ('NF EN 12976-1', 'EN 12976-1', 'fonc', 'Chauffe-eau solaires préfabriqués.'),
    'NM 06.1.100': ('NF C 15-100', 'IEC 60364 / HD 60364', 'fonc', 'Installations électriques basse tension.'),
    'NM 06.1.102': ('NF C 15-100', 'IEC 60364-3', 'fonc', 'Installations électriques basse tension.'),
    'NM 06.1.103': ('NF C 15-100', 'IEC 60364-4', 'fonc', 'Installations électriques basse tension.'),
    'NM 06.1.104': ('NF C 15-100', 'IEC 60364-5', 'fonc', 'Installations électriques basse tension.'),
    'NM 06.1.105': ('NF C 15-100', 'IEC 60364-6', 'fonc', 'Installations électriques basse tension.'),
    'NM 06.1.106': ('NF C 15-100', 'IEC 60364-7', 'fonc', 'Installations électriques basse tension.'),
    'NM 06.1.004': ('NF C 17-200', '', 'fonc', 'Installations d’éclairage public.'),
    'NM 21.9.502': ('NF S 61-919', '', 'fonc', 'Maintenance des extincteurs portatifs.'),
    'NM 21.9.014': ('Règle APSAD R4', '', 'fonc', 'Installation des extincteurs (référentiel assureurs, pas une norme).'),
    'NM 21.9.013': ('NF S 62-201 / Règle APSAD R5', 'EN 671-3', 'fonc', 'Installation des RIA.'),
}

def clean(s):
    s = s.replace('EuroCode marocaine :', 'Eurocode ').replace('Code marocaine :', 'code ')
    return re.sub(r'\s+', ' ', s).strip()

def equivalence(nm, eq):
    """Retourne (eu, fr, statut, note)."""
    if nm in CURATED:
        fr, eu, s, note = CURATED[nm]
        return eu, fr, s, note
    e = eq.strip()
    if not e:
        m = re.match(r'NM ((?:EN|ENV|CEN/TS|CEN/TR) .+)$', nm)
        if m: e = m.group(1)
    e = re.sub(r'\bCEI\b', 'IEC', e)
    if not e:
        return '', '', 'aucune', ''
    if re.match(r'(NF|XP|FD|DTU|NF DTU|T |P |B )', e):
        fr = e if not e.startswith(('T ', 'P ', 'B ')) else 'NF ' + e
        return '', fr, 'imanor', 'Référence française citée par IMANOR.'
    if re.match(r'(EN|ENV|CEN/TS|CEN/TR)\b', e):
        eu = e
        base = re.sub(r'\s*-\s*A\d.*$', '', e)  # « EN 206-1 - A1 et A2 »
        if e.startswith('EN'):
            return eu, 'NF ' + base, 'auto', 'Toute norme EN est reprise en France sous « NF EN » (même numéro). Vérifier l’édition et un éventuel complément national (/CN).'
        return eu, base.replace('CEN/', 'XP CEN/') + ' (si reprise)', 'verif', 'Spécification / rapport CEN : reprise française (XP, FD) à vérifier.'
    if re.match(r'ISO', e):
        return e, 'NF ' + e + ' ou NF EN ' + e + ' (si reprise)', 'verif', 'Norme ISO : reprise française possible en NF ISO ou NF EN ISO – à vérifier.'
    if re.match(r'IEC', e):
        num = re.sub(r'^IEC(/IEEE)? ', '', e)
        return e, 'NF EN ' + num + ' (si reprise CENELEC)', 'verif', 'Norme IEC : souvent reprise en EN 6xxxx par le CENELEC puis en NF EN – à vérifier.'
    return e, '', 'verif', ''

out = {}
for r in src:
    nm = clean(r['nm'])
    lot = r['sub'] or ('4.%d' % r['lot'])
    if nm in out:
        if lot not in out[nm]['l']:
            out[nm]['l'].append(lot)
        continue
    eu, fr, s, note = equivalence(nm, clean(r['eq']))
    out[nm] = dict(c=nm, e=clean(r['eq']), t=clean(r['titre']), d=clean(r['domaine']),
                   l=[lot], eu=eu, fr=fr, s=s, n=note)

recs = list(out.values())
stats = {}
for x in recs:
    stats[x['s']] = stats.get(x['s'], 0) + 1
payload = 'window.NORMES_LOTS=' + json.dumps(LOTS, ensure_ascii=False) + ';\n'
payload += 'window.NORMES=' + json.dumps(recs, ensure_ascii=False, separators=(',', ':')) + ';\n'
(ROOT / 'app/data').mkdir(parents=True, exist_ok=True)
(ROOT / 'app/data/normes.js').write_text(payload, encoding='utf-8')
print(len(recs), 'normes NM uniques', stats)
