# QI Business Pro — espace professeur (génération d'APK via GitHub Actions)

C'est la 2e application du projet QI Business, réservée aux professeurs — comme
Yango a une app "passager" et une app "chauffeur" (Yango Pro).

1. Crée un **nouveau dépôt GitHub** séparé de celui de l'app élève/parent (ex.
   `qi-business-pro`), puis dépose tout le contenu de ce dossier dedans.
2. Va dans l'onglet **Actions** : le workflow "Build APK" se lance automatiquement.
   S'il ne démarre pas, clique dessus puis "Run workflow".
3. Attends la fin (icône verte, ~4-6 minutes).
4. Clique sur le run terminé → section **Artifacts** → télécharge `qi-business-pro-apk`
   (contient `app-debug.apk`).
5. Décompresse, transfère l'APK sur le téléphone du professeur, autorise
   "Sources inconnues", installe.

## Ce qui fonctionne déjà (en local, sur l'appareil)
- Planning du jour, marquer une séance "en route" ou "terminée".
- Partage de position **réel** (vraie position GPS du téléphone) quand le
  professeur active "Disponibilité" — visible seulement sur son propre
  téléphone pour l'instant.
- Détail des gains avec répartition transparente professeur / commission
  QI Business (données de démonstration).
- Moyen de versement, matières, nom du profil.

## Ce qu'il reste à connecter pour que ce soit réel
- Un **back-end** (ex. Supabase) pour que la position du professeur soit
  visible par les parents/élèves de l'app QI Business en temps réel.
- Un service de **paiement mobile money avec répartition automatique**
  (ex. CinetPay, PayDunya) pour que la commission soit vraiment prélevée.
- Un **back office** admin pour valider les professeurs, gérer les litiges
  et suivre les commissions globales.
