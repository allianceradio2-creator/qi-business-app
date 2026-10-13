# QI Business — génération d'APK via GitHub Actions

1. Crée un dépôt GitHub (public ou privé), puis dépose tout le contenu de ce dossier dedans
   (glisser-déposer sur github.com, ou `git push`).
2. Va dans l'onglet **Actions** du dépôt : le workflow "Build APK" se lance automatiquement.
   S'il ne démarre pas, clique dessus puis "Run workflow".
3. Attends la fin (icône verte, ~4-6 minutes).
4. Clique sur le run terminé → section **Artifacts** en bas de page → télécharge `qi-business-apk`
   (c'est un .zip contenant `app-debug.apk`).
5. Décompresse, transfère `app-debug.apk` sur ton téléphone, autorise "Sources inconnues",
   installe et teste.

Pour republier une nouvelle version : remplace les fichiers dans `www/`, pousse à nouveau
sur `main`, le workflow refait un APK automatiquement.
