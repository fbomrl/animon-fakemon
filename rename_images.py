"""
Renomeia arquivos de imagem nas pastas do projeto animon-fakemon.
Ex: "001 - Myrmeflag.jpg" → "001.jpg"
Roda uma vez na raiz do projeto: python rename_images.py
"""
import os
import re

# Mapeamento: nome da pasta no disco
FOLDERS = [
    'Brasca', 'Dunnottar', 'Lekker', 'Rebueno',
    'Unknown', 'Zodiac', 'System Solar', 'Turtle', 'Paleta Mexicana'
]

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

for folder in FOLDERS:
    folder_path = os.path.join(base, folder)
    if not os.path.isdir(folder_path):
        print(f'⚠ Pasta não encontrada: {folder_path}')
        continue

    renamed = 0
    for filename in os.listdir(folder_path):
        name, ext = os.path.splitext(filename)
        ext = ext.lower()
        if ext not in ('.jpg', '.jpeg', '.png', '.webp'):
            continue

        # Extrai só os dígitos do início: "001 - Myrmeflag" → "001"
        m = re.match(r'^(\d+)', name.strip())
        if not m:
            print(f'  ⚠ Ignorado (sem número): {filename}')
            continue

        new_name = m.group(1).zfill(3) + ext
        if new_name == filename:
            continue  # já está no formato correto

        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)

        if os.path.exists(dst):
            print(f'  ⚠ Conflito (já existe): {new_name} em {folder}')
            continue

        os.rename(src, dst)
        print(f'  ✓ {folder}/{filename} → {new_name}')
        renamed += 1

    print(f'📁 {folder}: {renamed} arquivos renomeados')

print('\n✅ Concluído!')
