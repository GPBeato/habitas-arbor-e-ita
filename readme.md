# 🌳 Habitas - Sistema de Gestão de Arborização Urbana

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.1.2-green)](https://www.djangoproject.com/)
[![TailwindCSS](https://img.shields.io/badge/tailwindcss-3.2.0-38B2AC)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Habitas** é um sistema web completo para gestão colaborativa de arborização urbana, desenvolvido para a cidade de São José dos Campos/SP. O sistema permite mapeamento interativo, quantificação de serviços ecossistêmicos e gestão participativa envolvendo gestores públicos, técnicos especializados e cidadãos.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Características Principais](#-características-principais)
- [Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [Instalação](#-instalação)
  - [Windows](#windows)
  - [Linux/Mac](#linuxmac)
- [Uso do Sistema](#-uso-do-sistema)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Modelos de Cálculo](#-modelos-de-cálculo)
- [Funcionalidades](#-funcionalidades)

---

## 🌟 Sobre o Projeto

O **Habitas** é uma plataforma de gestão urbana de árvores que integra tecnologias web modernas com modelos científicos para quantificação de serviços ecossistêmicos. Inspirado no NYC Tree Maps, o sistema oferece:

- **Mapeamento interativo** de ~15.000 árvores cadastradas
- **Quantificação de benefícios ambientais** (CO₂, água, energia, biodiversidade)
- **Sistema colaborativo** com três níveis de usuários
- **Gestão de laudos técnicos** com fluxo de aprovação
- **Sistema de notificações** para problemas e eventos
- **Interface responsiva** e moderna

---

## ✨ Características Principais

### 🗺️ Visualização Interativa
- Mapa com todas as árvores de São José dos Campos
- Filtros por bairros usando análise geoespacial
- Informações detalhadas de cada árvore (espécie, DAP, altura, localização)
- Integração com Google Maps

### 🌿 Serviços Ecossistêmicos
- **Sequestro de CO₂**: Cálculo baseado em biomassa
- **Interceptação de água pluvial**: Estimativa anual
- **Conservação de energia**: Economia por sombreamento
- **Índice de biodiversidade**: Contribuição à fauna e flora

### 👥 Sistema Multi-nível
- **Nível 1 - Gestores**: Aprovação de técnicos, validação de laudos, resolução de notificações
- **Nível 2 - Técnicos**: Criação de laudos técnicos, análise de notificações
- **Nível 3 - Cidadãos**: Comentários, criação de notificações, participação comunitária

### 📊 Gestão Administrativa
- Dashboard personalizado por nível de usuário
- Sistema completo de laudos técnicos (CRUD)
- Gestão de notificações com fluxo de trabalho
- Histórico de ações e auditoria
- Sistema de comentários em tempo real

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 4.1.2** - Framework web Python
- **django-unicorn 0.49.2** - Componentes reativos
- **django-import-export 3.0.1** - Importação/exportação de dados
- **SQLite3** - Banco de dados

### Frontend
- **TailwindCSS 3.2.0** - Framework CSS utilitário
- **Leaflet.js 1.9.2** - Mapas interativos
- **Turf.js 6.x** - Análise geoespacial
- **JavaScript (ES6+)** - Interatividade

### Ferramentas
- **Python 3.8+**
- **Node.js & npm** - Gerenciamento de pacotes frontend
- **Git** - Controle de versão

---

## 📥 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Node.js e npm (para TailwindCSS)
- Git

### Windows

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/habitas-main.git
   cd habitas-main
   ```

2. **Instale o virtualenv**
   ```bash
   pip install virtualenv
   ```

3. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

4. **Instale as dependências Python**
   ```bash
   pip install -r requirements.txt
   ```

5. **Instale as dependências Node.js** (para TailwindCSS)
   ```bash
   cd habitas/jstoolchain
   npm install
   cd ../..
   ```

6. **Execute as migrações do banco de dados**
   ```bash
   cd habitas
   python manage.py migrate
   ```

7. **Crie um superusuário (administrador)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

9. **Acesse o sistema**
   - Aplicação: `http://localhost:8000`
   - Admin: `http://localhost:8000/admin`

### Linux/Mac

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/habitas-main.git
   cd habitas-main
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Instale as dependências Python**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instale as dependências Node.js**
   ```bash
   cd habitas/jstoolchain
   npm install
   cd ../..
   ```

5. **Execute as migrações**
   ```bash
   cd habitas
   python manage.py migrate
   ```

6. **Crie um superusuário**
   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor**
   ```bash
   python manage.py runserver
   ```

8. **Acesse o sistema**
   - Aplicação: `http://localhost:8000`
   - Admin: `http://localhost:8000/admin`

### Scripts de Inicialização Rápida

O projeto inclui scripts para facilitar o desenvolvimento:

```bash
# Iniciar Django + TailwindCSS (modo watch) simultaneamente
./start_dev.sh

# Ou iniciar separadamente:
./start_django.sh    # Apenas Django
./start_tailwind.sh  # Apenas TailwindCSS (modo watch)
```

---

## 💻 Uso do Sistema

### Para Cidadãos

1. **Cadastre-se** em `Cadastrar > Cidadão`
2. **Explore o mapa** e clique em uma árvore para ver detalhes
3. **Adicione comentários** sobre as árvores
4. **Crie notificações** para reportar problemas ou eventos

### Para Técnicos

1. **Cadastre-se** em `Cadastrar > Técnico` (aguarde aprovação do gestor)
2. Após aprovação, **acesse seu dashboard**
3. **Crie laudos técnicos** selecionando árvores no mapa
4. **Analise notificações** e forneça pareceres especializados
5. **Gerencie seus laudos** (editar enquanto pendente)

### Para Gestores

1. **Login com conta de gestor** (criada via admin)
2. **Aprove técnicos** cadastrados
3. **Valide laudos técnicos** (aprovar/rejeitar com feedback)
4. **Resolva notificações** após análise técnica
5. **Monitore estatísticas** no dashboard

---

## 📁 Estrutura do Projeto

```
habitas-main/
├── habitas/                      # Projeto Django
│   ├── habitas/                  # Configurações do projeto
│   │   ├── settings.py           # Configurações Django
│   │   ├── urls.py               # Rotas principais
│   │   └── wsgi.py               # Interface WSGI
│   ├── main/                     # App principal
│   │   ├── models.py             # Modelos de dados
│   │   ├── views.py              # Views e lógica
│   │   ├── forms.py              # Formulários
│   │   ├── admin.py              # Painel administrativo
│   │   ├── decorators.py         # Decoradores de permissão
│   │   ├── components/           # Componentes Unicorn
│   │   │   └── posts.py          # Sistema de comentários
│   │   ├── templates/            # Templates HTML
│   │   │   ├── _base.html        # Template base
│   │   │   ├── index.html        # Página principal (mapa)
│   │   │   ├── auth/             # Autenticação
│   │   │   ├── dashboards/       # Dashboards
│   │   │   ├── laudos/           # Sistema de laudos
│   │   │   ├── notificacoes/     # Sistema de notificações
│   │   │   └── gestao/           # Gestão de usuários
│   │   └── migrations/           # Migrações do banco
│   ├── static/                   # Arquivos estáticos
│   │   ├── css/                  # Estilos CSS
│   │   ├── js/                   # Scripts JavaScript
│   │   └── image/                # Imagens
│   ├── jstoolchain/              # Ferramentas Node.js
│   │   ├── package.json          # Dependências npm
│   │   └── tailwind.config.js    # Configuração Tailwind
│   ├── media/                    # Uploads de usuários
│   ├── db.sqlite3                # Banco de dados SQLite
│   └── manage.py                 # CLI Django
├── scripts/                      # Scripts utilitários
│   ├── scrape_trees.py           # Coleta de dados
│   └── salvar_banco.py           # Importação de dados
├── metrics/                      # Análises e métricas
├── requirements.txt              # Dependências Python
├── start_dev.sh                  # Script de desenvolvimento
├── start_django.sh               # Apenas Django
├── start_tailwind.sh             # Apenas TailwindCSS
├── trees_all.csv                 # Dataset de árvores
├── REGISTRO_DE_IMPLEMENTACOES.md # Documentação técnica
├── RESUMO_EXECUTIVO.md           # Resumo executivo
├── SISTEMA_NOTIFICACOES.md       # Doc. notificações
├── GUIA_NOTIFICACOES.md          # Guia de uso
└── readme.md                     # Este arquivo
```

---

## 📐 Modelos de Cálculo

### Sequestro de CO₂ (Schumacher & Hall, 1933)

Estimativa de biomassa e carbono armazenado:

$$
\ln{C} = \beta_0 + \beta_1 \ln{DAP} + \beta_2 \ln{H_t}
$$

**Parâmetros:**
```
β₀ = -0.906586 
β₁ = 1.60421 
β₂ = 0.37162
```

Onde:
- `C` = Carbono armazenado (kg)
- `DAP` = Diâmetro à Altura do Peito (cm)
- `H_t` = Altura total da árvore (m)

### Interceptação de Água Pluvial (Gash, 1979)

Modelo de interceptação de chuva pela copa das árvores, calculando volume anual de água retida.

### Conservação de Energia (Ko, 2018)

Estimativa de economia energética proporcionada pelo sombreamento e redução de temperatura ambiente.

### Índice de Biodiversidade

Cálculo proprietário baseado em:
- Diversidade de espécies
- Potencial de abrigo para fauna
- Produção de frutos/flores
- Contribuição ao ecossistema local

---

## 🎯 Funcionalidades

### Sistema de Autenticação
- ✅ Registro de cidadãos, técnicos e gestores
- ✅ Aprovação de técnicos por gestores
- ✅ Login/logout com sessões seguras
- ✅ Dashboards personalizados por nível

### Mapeamento de Árvores
- ✅ Visualização de ~15.000 árvores
- ✅ Marcadores interativos com popup
- ✅ Filtros por bairro (análise geoespacial)
- ✅ Estatísticas gerais e por região
- ✅ Informações detalhadas de cada árvore

### Sistema de Comentários
- ✅ Comentários em tempo real (django-unicorn)
- ✅ Menção a especialistas (@username)
- ✅ Histórico de interações
- ✅ Notificações visuais

### Sistema de Laudos Técnicos
- ✅ Criação de laudos por técnicos/gestores
- ✅ Upload de arquivos PDF
- ✅ Fluxo de aprovação (pendente → aprovado/rejeitado)
- ✅ Gestores fornecem feedback estruturado
- ✅ Técnicos podem editar laudos pendentes
- ✅ Visualização de laudos próprios e status
- ✅ Histórico completo de ações

### Sistema de Notificações
- ✅ Criação por cidadãos (denúncia/evento)
- ✅ Análise por técnicos com parecer
- ✅ Resolução por gestores
- ✅ Upload de fotos
- ✅ Histórico de mudanças de status
- ✅ Filtros avançados (status, tipo, técnico)
- ✅ Estatísticas em dashboard

### Gestão Administrativa
- ✅ Aprovação de técnicos cadastrados
- ✅ Validação de laudos com observações
- ✅ Resolução de notificações
- ✅ Dashboard com estatísticas
- ✅ Controle de permissões por nível

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos:

1. **Fork o projeto**
2. **Crie uma branch** para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. **Commit suas mudanças** (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push para a branch** (`git push origin feature/NovaFuncionalidade`)
5. **Abra um Pull Request**

### Diretrizes
- Siga o PEP 8 para código Python
- Escreva docstrings para funções e classes
- Adicione testes quando possível
- Mantenha o código limpo e legível
- Documente mudanças significativas

---

