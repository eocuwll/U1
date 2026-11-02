# Claude Usage Bar

Barre permanente en bas de claude.ai : `5 h : 23% (reset 14:00) | Semaine : 41% (reset lun. 09:00)`.
Vert < 70 %, orange 70–89 %, rouge ≥ 90 %. Rafraîchie toutes les 60 s.

## Installation

| Support | Étapes |
|---|---|
| PC (Chrome, Edge, Firefox) | 1. Installer **Tampermonkey**. 2. Nouveau script → coller `claude-usage-bar.user.js` → Enregistrer. 3. Recharger claude.ai. |
| Android | Navigateur **Firefox** + extension **Tampermonkey**, puis même procédure. Ouvrir claude.ai dans Firefox (pas dans l'app). |
| iPhone / iPad | App **Userscripts** (App Store, gratuite) → activer l'extension dans Safari → ajouter le script. Ouvrir claude.ai dans Safari. |

## Limites

- Les applications Claude natives (iOS, Android, Desktop) ne peuvent pas être modifiées. La barre ne fonctionne que dans un navigateur.
- Utilise un endpoint interne non documenté de claude.ai (`/api/organizations/{id}/usage`), celui de la page Paramètres > Utilisation. Il peut changer sans préavis : si la barre affiche « erreur », le script doit être mis à jour.
