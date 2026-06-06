# Animon Fakemon

Pokédex interativa dos fakemon (Animon) do universo Metanikk, integrada aos dados do DeviantArt.

**Website:** https://fbomrl.github.io/animon-fakemon

## Features

- **741 fakemon** carregados da planilha Excel
- **Dark mode** moderno com navegação por região
- **Filtros avançados:** tipo, região, busca por nome
- **Toggle PT-BR / EN** bilíngue
- **Ficha completa:** tipos, habilidades, altura, peso, habitat, alimentação, inspiração
- **Integração DeviantArt:** imagens e descrições coletadas automaticamente
- **Sincronização automática:** GitHub Actions roda daily às 03:00 UTC

## Estrutura do Repositório

```
animon-fakemon/
├── .github/
│   └── workflows/
│       └── sync-deviantart.yml        # GitHub Actions automation
├── data/
│   ├── animons.json                   # Dados de 741 animon
│   └── metadata.json                  # Metadata da última sync
├── scripts/
│   └── sync_deviantart.py             # Script Python de coleta
├── index.html                         # Dashboard (frontend)
└── Fakemon Region.xlsx                # Planilha com dados estruturados
```

## Dados

### animons.json

Cada animon tem:

```json
{
  "id": 1,
  "mr": 1,
  "regional": 1,
  "region": "Brasca",
  "name": "Myrmeflag",
  "type1": "Botanical",
  "type2": null,
  "species": "Little Anteater",
  "ability1": "Overgrow",
  "ability2": null,
  "ha": null,
  "height": "0.6",
  "weight": "11",
  "habitat": null,
  "feeding": null,
  "evo_by": null,
  "inspiration": "Tamanduá Bandeira",
  "emoji": "🌿",
  "image_url": null,
  "description_en": null,
  "description_pt": null,
  "deviantart_url": null,
  "last_updated": "2026-06-05T10:30:00Z"
}
```

### Regiões

- **Brasca** (🇧🇷): #1-200
- **Dunnottar** (🏴󠁧󠁢󠁳󠁣󠁴󠁿): #201-300
- **Lekker** (🌍): #301-501
- **Zodiac**: #502-513 (sem álbum DeviantArt)
- **Solar**: #514-522
- **Turtle**: #523-540
- **Unknown**: #541-746
- **Rebueno** (🇦🇷): #558-658
- **Paleta** (🇲🇽): #689-706

## Sincronização DeviantArt

O script `scripts/sync_deviantart.py`:

1. Carrega planilha Excel com dados estruturados
2. Busca DeviantArt por álbum (URL fixas)
3. Coleta imagens + descrições
4. Enriquece com dados da planilha como fallback
5. Gera `data/animons.json`

### Álbuns

- Brasca: https://www.deviantart.com/metanikk/gallery/57375612/brasca-region-first-generation
- Dunnottar: https://www.deviantart.com/metanikk/gallery/62148368/dunnottar-region-second-generation
- Lekker: https://www.deviantart.com/metanikk/gallery/64370949/lekker-region-third-generation
- Rebueno: https://www.deviantart.com/metanikk/gallery/70862073/rebueno-region-fourth-region
- Unknown: https://www.deviantart.com/metanikk/gallery/57136001/unknown-dex
- Solar: https://www.deviantart.com/metanikk/gallery/75262884/system-solar-dex
- Turtle: https://www.deviantart.com/metanikk/gallery/69802096/turtle-dex
- Paleta: https://www.deviantart.com/metanikk/gallery/78589649/paleta-mexicana-dex

## Desenvolvimento Local

### Rodar script de sync

```bash
cd scripts
python3 sync_deviantart.py
```

Gera/atualiza `data/animons.json`.

### Servir dashboard localmente

```bash
# Python 3
python3 -m http.server 8000

# Ou live-server (Node)
npx live-server
```

Abrir http://localhost:8000

## GitHub Pages

Configuração:

- Source: `Deploy from a branch`
- Branch: `main`
- Folder: `/ (root)`

Site atualiza automaticamente com cada push para `main`.

## Automação

GitHub Actions roda todo dia às 03:00 UTC:

```yaml
on:
  schedule:
    - cron: '0 3 * * *'
  workflow_dispatch  # Rodar manualmente
```

Para rodar manualmente: Actions tab → "Sync Animon Data" → Run workflow

## Tipos

Mapeamento de tipos:

| Oficial | Internal | PT-BR |
|---------|----------|-------|
| Grass | Botanical | Botânico |
| Water | Water | Água |
| Dark | Shadow | Sombrio |
| ... | ... | ... |

Veja `scripts/sync_deviantart.py` para lista completa.

## Contribuindo

Para adicionar novos animon:

1. Adicione à planilha Excel (`Fakemon Region.xlsx`)
2. Publique no DeviantArt (no álbum correto)
3. O script sincroniza automaticamente

## Histórico

- 2026-06-05: Initial setup com 741 animon
- GitHub Actions configurado para daily sync

---

**Criador:** Fabio (fbomrl)  
**Universo:** Metanikk Regions  
**Inspiração:** Pokédex oficial
