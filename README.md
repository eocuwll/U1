# Normathèque NM–EN

Application (HTML + APK Android) pour trouver une **norme marocaine NM** et sa correspondance **européenne (EN)** et **française (NF, NF EN, NF DTU)**, par mots-clés ou par domaine.

## Livrables

| Fichier | Usage |
|---|---|
| `app/index.html` (+ `app/data/`) | Application web, fonctionne hors ligne (ouvrir le fichier ou héberger le dossier `app/`) |
| `dist/Normes-NM-EN.apk` | Application Android 7.0+ (installer après avoir autorisé les sources inconnues) |

## Fonctions

- **Recherche** : mots-clés du chantier (agglo, regard, fer à béton, carrelage…), référence NM, EN ou NF. Filtres par lot IMANOR, nature (produit, essai, mise en œuvre) et fiabilité de l'équivalence.
- **Guide par domaine** : 17 domaines (béton, géotechnique, réseaux, électricité, routes, incendie…). Pour chacun : produits → essais → mise en œuvre (DTU) → calcul (Eurocodes), références FR/EU usuelles, mots-clés.
- **DTU & Eurocodes** : liste des NF DTU en vigueur (CSTB, juillet 2025) reliée aux NM qui les reprennent.
- **Favoris** (stockés sur l'appareil), copie de la référence, liens de recherche IMANOR / AFNOR.

## Données et fiabilité

- 1 634 normes NM uniques extraites du guide IMANOR *Conformité aux normes dans les achats publics*, édition 2023 V12 (`data/imanor_nm_2023.json`).
- Statut de chaque équivalence :

| Statut | Signification |
|---|---|
| Équivalence IMANOR | Référence NF/DTU citée par IMANOR |
| Même intitulé | NM nationale au titre identique à un texte français |
| EN → NF EN | Norme EN : reprise en France sous le même numéro |
| Équivalent fonctionnel | Même produit, textes différents : comparer avant de substituer |
| À vérifier | ISO / IEC / CEN-TS : reprise française possible, non confirmée |
| Pas d'équivalence connue | NM nationale sans correspondance dans la base |

Les éditions (année, amendements, compléments nationaux /CN) ne sont pas renseignées : vérifier chez IMANOR ou AFNOR avant prescription.

## Reconstruire

```bash
python3 tools/build_data.py        # data/imanor_nm_2023.json -> app/data/normes.js
./android/build_apk.sh             # -> dist/Normes-NM-EN.apk (JDK + Python, sans SDK Android)
python3 tools/build_artifact.py    # version page web hébergée
```

L'APK est assemblé sans SDK Android : `android.jar` (API 16), `dx` et `apksig` depuis Maven Central ; manifeste binaire et `resources.arsc` générés par `android/tools/package_apk.py`. Signature v2 avec la clé `android/normes-nmen.p12` (clé d'usage personnel ; mot de passe dans `build_apk.sh`). Garder la même clé pour pouvoir mettre à jour l'application installée.

---

## Annexe – Claude Code Skills

### Installed Skills

#### document-processing/pdf-processing-pro

Production-ready PDF processing toolkit installed at `~/.claude/skills/document-processing/pdf-processing-pro/`.

**Features:**
- PDF form analysis, filling, and validation
- Table extraction (CSV/Excel export)
- OCR processing for scanned PDFs
- Batch PDF operations
- Comprehensive error handling and logging

**Included scripts:**
- `analyze_form.py` - Extract form field information
- `fill_form.py` - Fill PDF forms with data
- `validate_form.py` - Validate form data before filling
- `extract_tables.py` - Extract tables to CSV/Excel
- `extract_text.py` - Extract text with formatting preservation
- `merge_pdfs.py` - Merge multiple PDFs
- `split_pdf.py` - Split PDF into individual pages
- `validate_pdf.py` - Validate PDF integrity

**Reference docs:**
- `FORMS.md` - Complete form processing guide
- `TABLES.md` - Advanced table extraction
- `OCR.md` - Scanned PDF processing

**Quick start:**
```bash
pip install pdfplumber pypdf pillow pytesseract pandas
python scripts/analyze_form.py input.pdf --output fields.json
```
