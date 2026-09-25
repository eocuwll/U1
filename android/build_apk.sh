#!/usr/bin/env bash
# Construit dist/Normes-NM-EN.apk sans SDK Android.
# Outils téléchargés depuis Maven Central : android.jar (API 16, compilation),
# dx 1.7 (conversion en DEX), apksig 2.3.0 (signature v2).
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$(pwd); B=$ROOT/android/build; T=$B/tools
VERSION_CODE=${VERSION_CODE:-1}; VERSION_NAME=${VERSION_NAME:-1.0}
KS=$ROOT/android/normes-nmen.p12; KS_PASS=${KS_PASS:-normes-nmen}
mkdir -p "$T" "$ROOT/dist"
M=https://repo.maven.apache.org/maven2
[ -f "$T/android.jar" ] || curl -sSfL -o "$T/android.jar" $M/com/google/android/android/4.1.1.4/android-4.1.1.4.jar
[ -f "$T/dx.jar" ]      || curl -sSfL -o "$T/dx.jar"      $M/com/google/android/tools/dx/1.7/dx-1.7.jar
[ -f "$T/apksig.jar" ]  || curl -sSfL -o "$T/apksig.jar"  $M/com/android/tools/build/apksig/2.3.0/apksig-2.3.0.jar

# 1. Application web embarquée
rm -rf "$B/www" "$B/classes" && mkdir -p "$B/www/data" "$B/classes"
cp app/index.html app/icon.svg app/manifest.webmanifest "$B/www/"
cp app/data/*.js "$B/www/data/"

# 2. Java -> .class (bytecode Java 6 attendu par dx 1.7) -> classes.dex
javac -nowarn --release 8 -cp "$T/android.jar" -d "$B/classes" android/src/ma/normes/nmen/*.java 2>&1 | grep -v "^warning\|^Picked\|^1 warning\|^Note" || true
find "$B/classes" -name '*.class' -exec python3 -c "
import sys
for f in sys.argv[1:]:
    d=bytearray(open(f,'rb').read()); d[6:8]=(50).to_bytes(2,'big'); open(f,'wb').write(d)" {} +
java -cp "$T/dx.jar" com.android.dx.command.Main --dex --output="$B/classes.dex" "$B/classes"

# 3. Paquet + signature
python3 android/tools/package_apk.py "$B/classes.dex" "$B/www" app/icon-192.png "$B/unsigned.apk" "$VERSION_CODE" "$VERSION_NAME"
if [ ! -f "$KS" ]; then
  keytool -genkeypair -keystore "$KS" -storetype PKCS12 -storepass "$KS_PASS" -keypass "$KS_PASS" \
    -alias nmen -keyalg RSA -keysize 2048 -validity 10000 -dname "CN=Normes NM-EN, O=Usage personnel, C=MA" 2>&1 | grep -v Picked || true
fi
javac -nowarn -cp "$T/apksig.jar" -d "$B/signer" android/tools/Signer.java 2>&1 | grep -v Picked || true
java --add-exports java.base/sun.security.x509=ALL-UNNAMED --add-exports java.base/sun.security.pkcs=ALL-UNNAMED --add-exports java.base/sun.security.util=ALL-UNNAMED -cp "$T/apksig.jar:$B/signer" Signer "$KS" "$KS_PASS" nmen "$B/unsigned.apk" "$ROOT/dist/Normes-NM-EN.apk" 2>&1 | grep -v Picked
ls -la "$ROOT/dist/Normes-NM-EN.apk"
