"""Vérifie que le logo QI Business est bien en place ; fait échouer la construction sinon (pour ne pas livrer une app sans logo)."""
import glob, os, sys
res = 'android/app/src/main/res'
bad = []
try:
    if 'qi_icon_background' not in open(res + '/mipmap-anydpi-v26/ic_launcher.xml', encoding='utf-8').read():
        bad.append("icône adaptative non remplacée")
except FileNotFoundError:
    bad.append("icône adaptative absente")
if glob.glob(res + '/drawable-v24/ic_launcher_foreground.xml'):
    bad.append("ancien calque d'icône Capacitor encore présent")
if not os.path.exists('branding/.splash_done'):
    bad.append("écrans de démarrage non remplacés")
if bad:
    print('ERREUR LOGO :', ' ; '.join(bad)); sys.exit(1)
print('Vérification du logo : OK (icône + écran de démarrage)')
