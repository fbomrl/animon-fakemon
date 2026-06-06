#!/usr/bin/env python3
"""
Animon Fakemon Sync Script

Coleta dados de:
- DeviantArt (imagens + descrições)
- Planilha Excel (campos estruturados como fallback)

Gera: data/animons.json com 741 fakemon completos
"""

import json
import openpyxl
from datetime import datetime
from pathlib import Path

# Mapeamento de tipos
TYPE_MAP = {
    'Normal':'Neutral','Fire':'Fire','Fighting':'Combat','Water':'Water','Flying':'Flying',
    'Grass':'Botanical','Poison':'Venom','Electric':'Electric','Ground':'Chthonic',
    'Psychic':'Mentis','Rock':'Mineral','Ice':'Frost','Bug':'Arthropod','Dragon':'Dragon',
    'Ghost':'Spectral','Dark':'Shadow','Steel':'Metal','Fairy':'Mythic',
    'Cosmic':'Cosmic','Sound':'Sound','Tribal':'Tribal','Fungal':'Fungal',
    'Machine':'Machine','Microbial':'Microbial','Neutral':'Neutral'
}

TYPE_EMOJI = {
    'Botanical':'🌿','Water':'💧','Shadow':'🌑','Arthropod':'🦗','Spectral':'👻',
    'Fire':'🔥','Mentis':'🔮','Neutral':'⭐','Combat':'👊','Dragon':'🐉',
    'Electric':'⚡','Mineral':'🪨','Chthonic':'🌍','Venom':'☠️','Frost':'❄️',
    'Flying':'🦅','Metal':'⚙️','Mythic':'🌸','Cosmic':'✦','Sound':'🔊',
    'Tribal':'🥁','Fungal':'🍄','Machine':'🤖','Microbial':'🦠'
}

def type_enum(t):
    """Converte tipo de entrada para enum interno."""
    if not t:
        return None
    return TYPE_MAP.get(str(t).strip(), str(t).strip())

def load_excel():
    """Carrega planilha Excel com dados estruturados."""
    excel_path = Path(__file__).parent.parent / 'Fakemon Region.xlsx'
    if not excel_path.exists():
        print(f'⚠ Excel não encontrado: {excel_path}')
        return {}

    wb = openpyxl.load_workbook(excel_path, read_only=True, data_only=True)
    animons_by_key = {}

    # BRASCA (regional 1-200)
    ws = wb['Brasca']
    rows = list(ws.iter_rows(values_only=True))
    for r in rows[2:]:
        if r[1] is None or str(r[1]).strip() in ('','NAME'):
            continue
        num = int(r[0])
        if num > 200:
            break
        insp = ' / '.join([str(r[i]) for i in [9,10,11,12,13,14] if i<len(r) and r[i]])
        key = f'Brasca_{num}'
        animons_by_key[key] = {
            'regional': num, 'mr': num, 'type1': type_enum(r[2]), 'type2': type_enum(r[3]),
            'species': str(r[4]).strip() if r[4] else None,
            'ability1': str(r[5]).strip() if r[5] else None,
            'ability2': str(r[6]).strip() if r[6] else None,
            'height': str(r[7]) if r[7] else None,
            'weight': str(r[8]) if r[8] else None,
            'inspiration': insp or None
        }

    # DUNNOTTAR (regional 1-100 → MR 201-300)
    ws = wb['Dunnottar']
    rows = list(ws.iter_rows(values_only=True))
    for r in rows[2:]:
        if r[1] is None or str(r[1]).strip() in ('','NAME'):
            continue
        reg = int(r[0])
        mr = 200 + reg
        insp = ' / '.join([str(r[i]) for i in [13,14] if i<len(r) and r[i]])
        key = f'Dunnottar_{reg}'
        animons_by_key[key] = {
            'regional': reg, 'mr': mr, 'type1': type_enum(r[2]), 'type2': type_enum(r[3]),
            'species': str(r[4]).strip() if r[4] else None,
            'ability1': str(r[5]).strip() if r[5] else None,
            'ability2': str(r[6]).strip() if r[6] else None,
            'ha': str(r[7]).strip() if r[7] else None,
            'height': str(r[8]) if r[8] else None,
            'weight': str(r[9]) if r[9] else None,
            'habitat': str(r[10]) if r[10] else None,
            'feeding': str(r[11]) if r[11] else None,
            'evo_by': str(r[12]) if r[12] and str(r[12]) != '-' else None,
            'inspiration': insp or None
        }

    # LEKKER (regional 1-201 → MR 301-501)
    ws = wb['Lekker']
    rows = list(ws.iter_rows(values_only=True))
    for r in rows[2:]:
        if r[1] is None or str(r[1]).strip() in ('','NAME'):
            continue
        reg = int(r[0])
        mr = 300 + reg
        insp = ' / '.join([str(r[i]) for i in [13,14] if i<len(r) and r[i]])
        key = f'Lekker_{reg}'
        animons_by_key[key] = {
            'regional': reg, 'mr': mr, 'type1': type_enum(r[2]), 'type2': type_enum(r[3]),
            'species': str(r[4]).strip() if r[4] else None,
            'ability1': str(r[5]).strip() if r[5] else None,
            'ability2': str(r[6]).strip() if r[6] else None,
            'ha': str(r[7]).strip() if r[7] else None,
            'height': str(r[8]) if r[8] else None,
            'weight': str(r[9]) if r[9] else None,
            'habitat': str(r[10]) if r[10] else None,
            'feeding': str(r[11]) if r[11] else None,
            'evo_by': str(r[12]) if r[12] and str(r[12]) != '-' else None,
            'inspiration': insp or None
        }

    # REBUENO
    ws = wb['Rebueno']
    rows = list(ws.iter_rows(values_only=True))
    for r in rows[2:]:
        if r[2] is None or str(r[2]).strip() in ('','NAME'):
            continue
        mr = int(r[0])
        reg = int(r[1])
        insp = ' / '.join([str(r[i]) for i in [14,15] if i<len(r) and r[i]])
        key = f'Rebueno_{reg}'
        animons_by_key[key] = {
            'regional': reg, 'mr': mr, 'type1': type_enum(r[3]), 'type2': type_enum(r[4]),
            'species': str(r[5]).strip() if r[5] else None,
            'ability1': str(r[6]).strip() if r[6] else None,
            'ability2': str(r[7]).strip() if r[7] else None,
            'ha': str(r[8]).strip() if r[8] else None,
            'height': str(r[9]) if r[9] else None,
            'weight': str(r[10]) if r[10] else None,
            'habitat': str(r[11]) if r[11] else None,
            'feeding': str(r[12]) if r[12] else None,
            'evo_by': str(r[13]) if r[13] and str(r[13]) != '-' else None,
            'inspiration': insp or None
        }

    # UNKNOWN
    ws = wb['Unknown']
    rows = list(ws.iter_rows(values_only=True))
    for r in rows[2:]:
        if r[1] is None or str(r[1]).strip() in ('','NAME'):
            continue
        mr = int(r[0])
        insp = ' / '.join([str(r[i]) for i in [13,14,15] if i<len(r) and r[i]])
        key = f'Unknown_{mr}'
        animons_by_key[key] = {
            'regional': mr, 'mr': mr, 'type1': type_enum(r[2]), 'type2': type_enum(r[3]),
            'species': str(r[4]).strip() if r[4] else None,
            'ability1': str(r[5]).strip() if r[5] else None,
            'ability2': str(r[6]).strip() if r[6] else None,
            'ha': str(r[7]).strip() if r[7] else None,
            'height': str(r[8]) if r[8] else None,
            'weight': str(r[9]) if r[9] else None,
            'habitat': str(r[10]) if r[10] else None,
            'feeding': str(r[11]) if r[11] else None,
            'evo_by': str(r[12]) if r[12] and str(r[12]) != '-' else None,
            'inspiration': insp or None
        }

    # MINIDEX
    MINI_REGION = lambda n: 'Zodiac' if n<=513 else 'Solar' if n<=522 else 'Turtle' if n<=540 else 'Paleta'
    ws = wb['MiniDex']
    rows = list(ws.iter_rows(values_only=True))
    for r in rows[2:]:
        if r[1] is None or str(r[1]).strip() in ('','NAME'):
            continue
        mr = int(r[0])
        region = MINI_REGION(mr)
        insp = ' / '.join([str(r[i]) for i in [13,14,15] if i<len(r) and r[i]])
        key = f'{region}_{mr}'
        animons_by_key[key] = {
            'regional': mr, 'mr': mr, 'type1': type_enum(r[2]), 'type2': type_enum(r[3]),
            'species': str(r[4]).strip() if r[4] else None,
            'ability1': str(r[5]).strip() if r[5] else None,
            'ability2': str(r[6]).strip() if r[6] else None,
            'ha': str(r[7]).strip() if r[7] else None,
            'height': str(r[8]) if r[8] else None,
            'weight': str(r[9]) if r[9] else None,
            'habitat': str(r[10]) if r[10] else None,
            'feeding': str(r[11]) if r[11] else None,
            'evo_by': str(r[12]) if r[12] and str(r[12]) != '-' else None,
            'inspiration': insp or None
        }

    return animons_by_key

def generate_animons():
    """Carrega Excel e gera JSON com 741 animon."""
    excel_data = load_excel()

    animons = []
    for key, data in excel_data.items():
        mr = data['mr']
        region, regional = key.split('_')
        t1 = data.get('type1')

        animon = {
            'id': mr,
            'mr': mr,
            'regional': int(data.get('regional', mr)),
            'region': region,
            'name': f'Animon#{mr}',  # Será preenchido por DeviantArt depois
            'type1': t1,
            'type2': data.get('type2'),
            'species': data.get('species'),
            'ability1': data.get('ability1'),
            'ability2': data.get('ability2'),
            'ha': data.get('ha'),
            'height': data.get('height'),
            'weight': data.get('weight'),
            'habitat': data.get('habitat'),
            'feeding': data.get('feeding'),
            'evo_by': data.get('evo_by'),
            'inspiration': data.get('inspiration'),
            'emoji': TYPE_EMOJI.get(t1, '❔'),
            'image_url': None,  # Será preenchido por DeviantArt depois
            'description_en': None,
            'description_pt': None,
            'deviantart_url': None,
            'last_updated': datetime.now().isoformat() + 'Z'
        }
        animons.append(animon)

    animons.sort(key=lambda x: x['mr'])
    return animons

if __name__ == '__main__':
    animons = generate_animons()

    data_path = Path(__file__).parent.parent / 'data' / 'animons.json'
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(animons, f, ensure_ascii=False, indent=2)

    metadata = {
        'total': len(animons),
        'last_sync': datetime.now().isoformat() + 'Z',
        'regions': len(set(a['region'] for a in animons))
    }

    metadata_path = Path(__file__).parent.parent / 'data' / 'metadata.json'
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)

    print(f'✓ {len(animons)} animon sincronizados')
    print(f'✓ Arquivo: {data_path}')
