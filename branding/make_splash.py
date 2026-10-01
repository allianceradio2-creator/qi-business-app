"""Remplace l'écran de démarrage par défaut de Capacitor par le logo QI Business (même dimensions que chaque fichier)."""
import glob
from PIL import Image
logo = Image.open('branding/logo.png').convert('RGB')
n = 0
for p in glob.glob('android/app/src/main/res/drawable*/splash*.png'):
    w, h = Image.open(p).size
    canvas = Image.new('RGB', (w, h), (255, 255, 255))
    s = int(min(w, h) * 0.55)
    canvas.paste(logo.resize((s, s), Image.LANCZOS), ((w - s) // 2, (h - s) // 2))
    canvas.save(p)
    n += 1
print('écrans de démarrage remplacés :', n)
