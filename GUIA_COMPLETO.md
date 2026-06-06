# Guia Completo — Animon Fakemon

**Projeto:** Dashboard Pokédex dos fakemon Metanikk  
**GitHub pessoal:** https://github.com/fbomrl/animon-fakemon  
**Website final:** https://fbomrl.github.io/animon-fakemon  

---

## SITUAÇÃO ATUAL

O projeto já foi implementado e está salvo em:
```
/Users/fmeirelesdsi/projetos/animon-fakemon/
```

### O que já existe pronto:

| Arquivo | O que é |
|---|---|
| `index.html` | Dashboard completo com 741 animon, dark mode, filtros, modal |
| `data/animons.json` | 741 animon carregados da planilha Excel |
| `data/metadata.json` | Info da última sincronização |
| `scripts/sync_deviantart.py` | Script Python que lê Excel e gera o JSON |
| `.github/workflows/sync-deviantart.yml` | GitHub Actions — roda script diariamente |
| `Fakemon Region.xlsx` | Planilha com todos os dados dos fakemon |
| `README.md` | Documentação técnica |
| `.gitignore` | Arquivos ignorados pelo Git |

### O que ainda NÃO foi feito:
- Push para o GitHub pessoal (precisa das credenciais do usuário)
- Ativação do GitHub Pages
- Integração real com DeviantArt (imagens e descrições)

---

## PARTE 1: PUBLICAR NO GITHUB PESSOAL

### Pré-requisito
O usuário precisa:
1. Ter criado o repositório em: https://github.com/new
   - Nome: `animon-fakemon`
   - Público
   - Vazio (sem README)

2. Ter um **Personal Access Token** do GitHub pessoal:
   - https://github.com/settings/tokens
   - Scope mínimo: `repo`

### Comandos para executar (no terminal do usuário)

```bash
# Entrar na pasta do projeto
cd /Users/fmeirelesdsi/projetos/animon-fakemon

# Configurar credenciais PESSOAIS neste repo
git config user.name "Fabio"
git config user.email "SEU_EMAIL_PESSOAL@gmail.com"  # substituir

# Conectar ao GitHub pessoal
git remote add origin https://github.com/fbomrl/animon-fakemon.git

# Verificar
git remote -v

# Fazer push
git push -u origin main
# Quando pedir senha: colar o Personal Access Token
```

### Ativar GitHub Pages

1. Acessar: https://github.com/fbomrl/animon-fakemon/settings/pages
2. Source: `Deploy from a branch`
3. Branch: `main` / Folder: `/ (root)`
4. Clicar Save
5. Aguardar ~2 minutos

**Website disponível em:** https://fbomrl.github.io/animon-fakemon

---

## PARTE 2: INTEGRAÇÃO COM DEVIANTART (próxima etapa)

Esta parte adiciona imagens reais e descrições do DeviantArt ao dashboard.

### Contexto

Cada animon no DeviantArt tem:
- **Título:** `"001 - Myrmeflag"` (número regional + nome)
- **Descrição:** campos estruturados (Type, Ability, Species, etc.) + texto descritivo PT-BR e EN
- **Imagem:** URL direta acessível

### Formato da descrição (padrão novo — ex: Pinocchevil)

```
# 116 (#Unknowndex)
# 770 (#MetanikRegions)

Name: Pinocchevil
Type: Grass/Dark
Ability: Head Rip
HA: Does not have
Species: Cursed Doll
Height: 1,40
Weight: 30 kg
Gender Ratio: Genderless
Habitat: Forests
Feeding: Omnivorous
Evolution: Does not have

Descrição: [texto em português]
Description: [texto em inglês]
Inspiração: [inspiração]
Inspiration: [inspiration]
```

### Formato antigo (ex: Myrmeflag — Brasca)

- Estrutura parcial (sem Gender/Habitat/Feeding/HA)
- Número regional no título: `"001 - Myrmeflag"`
- Só descrição em inglês
- Campos faltantes: usar dados da planilha Excel como fallback

### Álbuns DeviantArt por região

| Região | URL | Obs |
|---|---|---|
| Brasca | https://www.deviantart.com/metanikk/gallery/57375612/brasca-region-first-generation | 1ª imagem = banner, ignorar |
| Dunnottar | https://www.deviantart.com/metanikk/gallery/62148368/dunnottar-region-second-generation | 1ª imagem = banner, ignorar |
| Lekker | https://www.deviantart.com/metanikk/gallery/64370949/lekker-region-third-generation | 1ª imagem = banner, ignorar |
| Rebueno | https://www.deviantart.com/metanikk/gallery/70862073/rebueno-region-fourth-region | 1ª imagem = banner, ignorar |
| Unknown | https://www.deviantart.com/metanikk/gallery/57136001/unknown-dex | SEM banner |
| Zodiac | — | Sem álbum no DeviantArt |
| Solar | https://www.deviantart.com/metanikk/gallery/75262884/system-solar-dex | 1ª imagem = banner, ignorar |
| Turtle | https://www.deviantart.com/metanikk/gallery/69802096/turtle-dex | 1ª imagem = banner, ignorar |
| Paleta | https://www.deviantart.com/metanikk/gallery/78589649/paleta-mexicana-dex | 1ª imagem = banner, ignorar |

### Regras de matching (planilha ↔ DeviantArt)

- Extrair número regional do título: `"001 - Myrmeflag"` → `001`
- Identificar região pelo álbum de origem
- Para formato novo: usar `#MetanikRegions` do corpo da descrição
- **NUNCA** fazer matching por posição — alguns fakemon estão na planilha mas não no DeviantArt

### O que fazer quando não encontra no DeviantArt

- `image_url`: null → dashboard exibe emoji do tipo
- `description_en` / `description_pt`: null → campo não exibe
- Dados estruturados: vêm 100% da planilha Excel

### Como implementar o script de coleta DeviantArt

O arquivo `scripts/sync_deviantart.py` já existe com a lógica da planilha Excel.
A IA responsável por esta etapa deve:

1. **Adicionar autenticação OAuth DeviantArt**
   - Criar app em: https://www.deviantart.com/developers/
   - Obter `client_id` e `client_secret`
   - Implementar fluxo OAuth 2.0 para obter access token
   - Armazenar token como GitHub Secret: `DEVIANTART_TOKEN`

2. **Implementar função `fetch_album_deviations(album_url)`**
   - Usar DeviantArt API: `GET /api/v1/gallery/folder`
   - Parâmetros: `folderid`, `username=metanikk`, `limit=24`, `offset=0`
   - Paginar até buscar todas as deviations
   - Retornar lista: `[{title, description, image_url, url}]`

3. **Implementar função `parse_description(text)`**
   - Procurar padrões: `Name:`, `Type:`, `Ability:`, `HA:`, `Species:`, `Height:`, `Weight:`, `Habitat:`, `Feeding:`, `Evolution:`
   - Extrair `Descrição:` (PT-BR) e `Description:` (EN) como blocos de texto
   - Retornar dict com campos extraídos
   - Ignorar campos desconhecidos (ataques, etc.)

4. **Implementar função `enrich_with_deviantart(animons, deviations)`**
   - Para cada deviation: extrair número do título + região do álbum
   - Buscar animon correspondente no JSON pelo MR/regional
   - Preencher: `image_url`, `description_en`, `description_pt`, `deviantart_url`
   - Manter dados da planilha como fallback para campos ausentes

5. **Atualizar GitHub Actions** para passar `DEVIANTART_TOKEN` como env var

### Mapeamento de tipos (para conversão automática)

```python
TYPE_MAP = {
    'Normal': 'Neutral',
    'Fire': 'Fire',
    'Fighting': 'Combat',
    'Water': 'Water',
    'Flying': 'Flying',
    'Grass': 'Botanical',
    'Poison': 'Venom',
    'Electric': 'Electric',
    'Ground': 'Chthonic',
    'Psychic': 'Mentis',
    'Rock': 'Mineral',
    'Ice': 'Frost',
    'Bug': 'Arthropod',
    'Dragon': 'Dragon',
    'Ghost': 'Spectral',
    'Dark': 'Shadow',
    'Steel': 'Metal',
    'Fairy': 'Mythic',
    'Cosmic': 'Cosmic',
    'Sound': 'Sound',
    'Tribal': 'Tribal',
    'Fungal': 'Fungal',
    'Machine': 'Machine',
    'Microbial': 'Microbial'
}
```

---

## PARTE 3: ESTRUTURA DOS DADOS

### Numeração MetanikRegions (MR)

| Região | Regional | MR | Cálculo |
|---|---|---|---|
| Brasca | 1-200 | 1-200 | MR = Regional |
| Dunnottar | 1-100 | 201-300 | MR = 200 + Regional |
| Lekker | 1-201 | 301-501 | MR = 300 + Regional |
| Zodiac | — | 502-513 | Fixo na planilha |
| Solar | — | 514-522 | Fixo na planilha |
| Turtle | — | 523-540 | Fixo na planilha |
| Unknown | — | 541-746 | Fixo na planilha |
| Rebueno | 1-101 | 558-658 | Fixo na planilha |
| Paleta | — | 689-706 | Fixo na planilha |

### Schema do animons.json

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
  "inspiration": "Tamanduá Bandeira (Myrmecophaga tridactyla)",
  "emoji": "🌿",
  "image_url": null,
  "description_en": null,
  "description_pt": null,
  "deviantart_url": null,
  "last_updated": "2026-06-05T00:00:00Z"
}
```

### Planilha Excel — estrutura das abas

**Brasca** (colunas: `#, NAME, TYPE 1, TYPE 2, SPECIES, ABILITIES 1, ABILITIES 2, H, W, INSPIRAÇÃO`)
- Sem HA, Habitat, Feeding (colunas ausentes — tratar como null)
- 200 fakemon com dados (ignorar linhas sem NAME)

**Dunnottar / Lekker** (colunas: `#, NAME, TYPE 1, TYPE 2, SPECIES, ABILITIES 1, ABILITIES 2, HIDDEN ABILITIES, H, W, HABITAT, FEEDING, EVO BY, INSPIRAÇÃO`)

**Rebueno** (colunas: `MR#, Regional#, NAME, TYPE 1, TYPE 2, SPECIES, ABILITIES 1, ABILITIES 2, HIDDEN ABILITIES, H, W, HABITAT, FEEDING, EVO BY, INSPIRAÇÃO`)
- Tem duas colunas de número (MR e Regional)

**Unknown** (igual Dunnottar, mas coluna `#` já é o MR)

**MiniDex** (igual Dunnottar, coluna `#` já é o MR)
- Zodiac: MR 502-513
- Solar: MR 514-522
- Turtle: MR 523-540
- Paleta Mexicana: MR 689-706

---

## PARTE 4: DASHBOARD (index.html)

### Funcionalidades implementadas

- Grid responsivo com todos os animon
- Barra de navegação por região (bandeiras por país de inspiração)
- Filtros por tipo (badges coloridas)
- Busca por nome (tempo real)
- Toggle PT-BR / EN (troca labels, tipos e descrições)
- Modal com ficha completa ao clicar no card
- Emoji de tipo como placeholder de imagem

### Bandeiras por região

| Região | Bandeira | Inspiração |
|---|---|---|
| Brasca | 🇧🇷 | Brasil |
| Dunnottar | 🏴󠁧󠁢󠁳󠁣󠁴󠁿 | Escócia |
| Lekker | 🌍 | África |
| Rebueno | 🇦🇷 | Argentina |
| Unknown | ❓ | — |
| Zodiac | ♈ | — |
| Solar | 🪐 | — |
| Turtle | 🐢 | — |
| Paleta | 🇲🇽 | México |

### Para adicionar imagens reais do DeviantArt

Quando `image_url` for preenchido no JSON, substituir no `index.html`:

```javascript
// Atual (emoji placeholder)
<div class="cimg">${a.emoji}</div>

// Após integração DeviantArt
<div class="cimg">
  ${a.image_url
    ? `<img src="${a.image_url}" alt="${a.name}" onerror="this.parentElement.textContent='${a.emoji}'">`
    : a.emoji}
</div>
```

---

## PARTE 5: CHECKLIST FINAL

### Deploy inicial (Parte 1)
- [ ] Repositório criado em https://github.com/fbomrl/animon-fakemon (público, vazio)
- [ ] Personal Access Token gerado (scope: repo)
- [ ] `cd /Users/fmeirelesdsi/projetos/animon-fakemon`
- [ ] `git config user.email "EMAIL_PESSOAL"`
- [ ] `git remote add origin https://github.com/fbomrl/animon-fakemon.git`
- [ ] `git push -u origin main`
- [ ] GitHub Pages ativado em Settings → Pages
- [ ] Website acessível em https://fbomrl.github.io/animon-fakemon
- [ ] 741 animon aparecendo no grid
- [ ] Filtros e busca funcionando
- [ ] Modal abre ao clicar no card

### Integração DeviantArt (Parte 2 — próxima sessão)
- [ ] App criado em https://www.deviantart.com/developers/
- [ ] OAuth implementado no script Python
- [ ] Função `fetch_album_deviations()` implementada
- [ ] Função `parse_description()` implementada
- [ ] Função `enrich_with_deviantart()` implementada
- [ ] Script testado localmente — JSON gerado com imagens
- [ ] `DEVIANTART_TOKEN` adicionado como GitHub Secret
- [ ] GitHub Actions atualizado com env var do token
- [ ] GitHub Actions rodando com sucesso (workflow_dispatch)
- [ ] Imagens aparecendo no dashboard
- [ ] Descrições PT-BR e EN aparecendo no modal

---

## OBSERVAÇÕES IMPORTANTES

1. **Brasca não tem HA/Habitat/Feeding** na planilha — é intencional. Será atualizada pelo usuário futuramente.

2. **Zodiac não tem álbum no DeviantArt** — ficará só com dados da planilha e emoji placeholder.

3. **Descrições em inglês apenas** (fakemon antigos) — manter como está. Usuário corrigirá depois.

4. **Fakemon na planilha sem DeviantArt** — usar dados da planilha. `image_url = null`.

5. **1ª imagem de cada álbum é banner** de apresentação — sempre ignorar ao iterar.

6. **Unknown Dex não tem banner** — não pular 1ª imagem.

7. **Rate limiting DeviantArt** — implementar delay de 0.5s entre requests.
