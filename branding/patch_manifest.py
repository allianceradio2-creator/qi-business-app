"""Ajoute les autorisations Android nécessaires au projet généré par `npx cap add android`."""
p = 'android/app/src/main/AndroidManifest.xml'
s = open(p, encoding='utf-8').read()
add = ''
for perm in ('android.permission.ACCESS_FINE_LOCATION', 'android.permission.ACCESS_COARSE_LOCATION'):
    if perm not in s:
        add += '    <uses-permission android:name="%s" />\n' % perm
if 'android.media.action.IMAGE_CAPTURE' not in s:
    add += '    <queries>\n        <intent>\n            <action android:name="android.media.action.IMAGE_CAPTURE" />\n        </intent>\n    </queries>\n'
s = s.replace('</manifest>', add + '</manifest>')
open(p, 'w', encoding='utf-8').write(s)
print('Manifest mis à jour :', 'localisation + appareil photo')
