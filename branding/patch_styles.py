"""Écran de démarrage Android 12+ : remplace l'icône par défaut de Capacitor par l'emblème QI Business."""
import os, re
from PIL import Image
res = 'android/app/src/main/res'
emb = Image.open('branding/emblem.png').convert('RGBA')
size = 432
canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
w = int(size * 0.60); h = int(w * emb.height / emb.width)
canvas.alpha_composite(emb.resize((w, h), Image.LANCZOS), ((size - w) // 2, (size - h) // 2))
os.makedirs(res + '/drawable', exist_ok=True)
canvas.save(res + '/drawable/splash_icon.png')
p = res + '/values/styles.xml'
s = open(p, encoding='utf-8').read()
m = re.search(r'(<style name="AppTheme\.NoActionBarLaunch"[^>]*parent="Theme\.SplashScreen"[^>]*>)', s)
if m and 'windowSplashScreenBackground' not in s:
    s = s.replace(m.group(1), m.group(1) + '\n        <item name="windowSplashScreenBackground">#FFFFFF</item>\n        <item name="windowSplashScreenAnimatedIcon">@drawable/splash_icon</item>', 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('styles.xml : écran de démarrage Android 12+ mis à jour')
else:
    print('styles.xml : style de démarrage Theme.SplashScreen non trouvé, rien modifié')
