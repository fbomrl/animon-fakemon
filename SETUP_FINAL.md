# Instruções Finais: Deploy para GitHub Pessoal

Projeto implementado e pronto. Você precisa fazer apenas **3 passos** para publicar no seu repo:

---

## Passo 1: Clonar do repositório que criei para o seu

```bash
# Volte para seu diretório de trabalho
cd ~/projetos  # ou o local que preferir

# Copie a pasta animon-fakemon
cp -r /tmp/animon-fakemon ./animon-fakemon-pronto
cd animon-fakemon-pronto
```

## Passo 2: Reconfigurar Git com suas credenciais pessoais

```bash
# IMPORTANTE: Usar suas credenciais PESSOAIS (não profissionais)
git config user.name "Seu Nome"
git config user.email "seu-email-pessoal@github.com"

# Verificar
git config --local user.email
```

## Passo 3: Adicionar remote do seu repositório GitHub

```bash
# Adicionar remote apontando para seu repo pessoal
git remote add origin https://github.com/fbomrl/animon-fakemon.git

# Verificar
git remote -v
# Deve mostrar:
# origin  https://github.com/fbomrl/animon-fakemon.git (fetch)
# origin  https://github.com/fbomrl/animon-fakemon.git (push)
```

## Passo 4: Fazer push para GitHub

```bash
# Push branch main
git push -u origin main

# Pode pedir seu token de autenticação (no lugar de senha):
# Gerar em: https://github.com/settings/tokens
# (Personal access token → repo scope)
```

---

## O que foi implementado

✅ **data/animons.json** — 741 animon com estrutura completa  
✅ **index.html** — Dashboard dark mode com 741 animon carregados  
✅ **scripts/sync_deviantart.py** — Script Python de sync (executável manual)  
✅ **GitHub Actions workflow** — Automação daily (roda em background)  
✅ **.gitignore** — Configuração padrão  
✅ **README.md** — Documentação completa  
✅ **Fakemon Region.xlsx** — Planilha versionada  

## Próximo: GitHub Pages

Após fazer push:

1. Ir para https://github.com/fbomrl/animon-fakemon/settings/pages
2. Source: `Deploy from a branch`
3. Branch: `main`
4. Folder: `/ (root)`
5. Save

Em ~1-2 minutos, estará em: **https://fbomrl.github.io/animon-fakemon**

---

## Testes locais (opcional)

Antes de fazer push, pode testar:

```bash
# Servir HTML localmente
python3 -m http.server 8000

# Abrir http://localhost:8000 no browser
# Testar filtros, busca, modal, toggle PT/EN
```

---

## Se tiver problemas com autenticação GitHub

Se der erro de autenticação no `git push`:

### Opção A: Token (recomendado)

1. Gerar token em: https://github.com/settings/tokens
2. Scope: `repo` (full control of private repositories)
3. Colar token no lugar da senha quando pedir

### Opção B: SSH

```bash
# Gerar chave SSH (se não tiver)
ssh-keygen -t ed25519 -C "seu-email@github.com" -f ~/.ssh/github_pessoal

# Adicionar em: https://github.com/settings/ssh/new
# Conteúdo de ~/.ssh/github_pessoal.pub

# Configurar Git para usar SSH
git config url."git@github.com:".insteadOf "https://github.com/"
```

---

## Fluxo após deploy

1. Website estará em: https://fbomrl.github.io/animon-fakemon
2. GitHub Actions roda todo dia às 03:00 UTC
3. Quando adicionar animon no Excel + DeviantArt, script sincroniza automaticamente
4. Mudanças no `data/animons.json` são commitadas automaticamente

---

## Checklist final

- [ ] Repo criado em https://github.com/fbomrl/animon-fakemon
- [ ] Arquivos copiados de `/tmp/animon-fakemon-pronto`
- [ ] Git configurado com credenciais pessoais
- [ ] Remote adicionado corretamente
- [ ] Push feito para main
- [ ] GitHub Pages ativado em Settings
- [ ] Website acessível em https://fbomrl.github.io/animon-fakemon
- [ ] Dashboard carrega 741 animon corretamente
- [ ] Filtros (tipo, região) funcionando
- [ ] Busca funcionando
- [ ] Toggle PT/EN funcionando
- [ ] Modal abre ao clicar em card

---

**Pronto!** Após completar esses passos, seu dashboard estará 100% online e funcional.

Qualquer dúvida, consulte o README.md do projeto.
