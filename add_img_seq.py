"""
Adiciona campo img_seq ao animons.json para todas as regiões.
img_seq = número sequencial da imagem na pasta (1, 2, 3...)
Para regiões normais (Brasca, Dunnottar, Lekker, Rebueno): img_seq = regional
Para regiões com buracos/offset (Unknown, Zodiac, Solar, Turtle, Paleta): 
  img_seq = posição sequencial ordenada por MR dentro da região
"""
import json

data = json.load(open('data/animons.json', encoding='utf-8'))

# Regiões com numeração sequencial simples (regional já é correto)
SIMPLE_REGIONS = {'Brasca', 'Dunnottar', 'Lekker', 'Rebueno'}

# Regiões que precisam de sequência calculada
SEQUENTIAL_REGIONS = {'Unknown', 'Zodiac', 'Solar', 'Turtle', 'Paleta'}

# Para regiões sequenciais: ordena por MR e atribui 1, 2, 3...
seq_map = {}  # (region, mr) -> img_seq
for region in SEQUENTIAL_REGIONS:
    items = sorted([a for a in data if a['region'] == region], key=lambda x: x['mr'])
    for i, a in enumerate(items, start=1):
        seq_map[(region, a['mr'])] = i
        print(f"  {region} mr={a['mr']} {a['name']} -> img_seq={i}")

# Aplica img_seq a todos
for a in data:
    if a['region'] in SIMPLE_REGIONS:
        a['img_seq'] = a['regional']
    elif a['region'] in SEQUENTIAL_REGIONS:
        a['img_seq'] = seq_map.get((a['region'], a['mr']), None)
    else:
        a['img_seq'] = a['regional']

with open('data/animons.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n✅ img_seq adicionado a {len(data)} animon')

# Verifica Unknown
unknown = sorted([a for a in data if a['region']=='Unknown'], key=lambda x: x['mr'])
print('\nVerificação Unknown:')
for a in unknown[:5]:
    print(f"  mr={a['mr']} {a['name']} -> img_seq={a['img_seq']}")
print('  ...')
for a in unknown[15:20]:
    print(f"  mr={a['mr']} {a['name']} -> img_seq={a['img_seq']}")
