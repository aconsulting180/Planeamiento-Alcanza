import re

with open('Planeamiento_2026.html','r',encoding='utf-8') as f:
    html=f.read()

print('File length:', len(html))

tags = set(re.findall(r'area-tag\.(\w+)', html))
print('Area tags:', sorted(tags))

sk = re.search(r"const SK='([^']+)'", html)
print('Storage key:', sk.group(1) if sk else 'NOT FOUND')

mp = re.search(r'const map=\[([^\]]+)\]', html)
print('showPage map:', mp.group(1)[:200] if mp else 'NOT FOUND')

# Check exportAll
ex = re.search(r"\['gis'[^\]]*\]\.forEach\(key=>", html)
print('exportAll:', ex.group(0) if ex else 'NOT FOUND')

# Check state
st = re.search(r'la:\{([^}]+)\}', html)
print('State la:', st.group(1)[:200] if st else 'NOT FOUND')

# Check seeds
seeds = re.findall(r'const (\w+_SEED)\s*=', html)
print('Seeds:', seeds)

# Check if rental already exists
print('Has rental:', 'rental' in html.lower())
