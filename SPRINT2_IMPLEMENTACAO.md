# Sprint 2 - Implementação Completa ✅

## 🌳 Interface Configurável + 2 Novos Serviços Ecossistêmicos

### ✅ O que foi implementado

1. **Sistema de Configuração Dinâmica**
   - ✅ Modelo `EcosystemServiceConfig` para serviços configuráveis
   - ✅ Modelo `EcosystemServiceHistory` para histórico de mudanças
   - ✅ Admin Django customizado para gestores (Nível 1)
   - ✅ Refatoração dos cálculos para usar configurações do BD

2. **Novos Serviços Ecossistêmicos**
   - ✅ Remoção de PM2.5 (i-Tree simplificado)
   - ✅ Remoção de O₃ (i-Tree simplificado)
   - ✅ Absorção Anual de Carbono (novo serviço diferenciado)

3. **Documentação**
   - ✅ Documento científico completo (`METODOLOGIAS_SERVICOS_ECOSSISTEMICOS.md`)

---

## 📋 Como Executar

### 1. Ativar Ambiente Virtual

```bash
# No diretório raiz do projeto
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 2. Instalar Dependências (se necessário)

```bash
# Se tiver problema com orjson (requer Rust), você pode:
# - Instalar Rust: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
# - Ou comentar temporariamente a linha no requirements.txt
pip install -r requirements.txt
```

### 3. Criar Migração

```bash
cd habitas
python manage.py makemigrations main
```

### 4. Aplicar Migração

```bash
python manage.py migrate
```

### 5. Popular Serviços Iniciais

```bash
python manage.py init_ecosystem_services
```

Isso criará:
- ✅ Armazenamento de CO₂ (Schumacher & Hall, 1933)
- ✅ Interceptação de Água Pluvial (Gash, 1979)
- ✅ Conservação de Energia (Ko, 2018)
- ✅ Índice de Biodiversidade
- ✅ Remoção de PM2.5 (NOVO)
- ✅ Remoção de O₃ (NOVO)
- ✅ Absorção Anual de Carbono (NOVO)

### 6. Testar Compatibilidade

```bash
python manage.py test_compatibility
```

Este comando verifica se os valores calculados via BD são idênticos aos métodos antigos (@property).

---

## 🎯 Como Usar o Admin Customizado

### Acesso

1. **Faça login como gestor** (usuário com `user_type='GESTOR'`)
2. **Acesse** `/admin/`
3. **Navegue até** "Configurações de Serviços Ecossistêmicos"

### Funcionalidades

#### ✅ Editar Serviço Existente

1. Clique em um serviço existente
2. Edite:
   - **Fórmula**: Código Python (use `dap`, `altura`, `biomassa`, `tree`, `coeficientes`)
   - **Coeficientes**: JSON com parâmetros (ex: `{"BETA0": -0.906586}`)
   - **Valor Monetário**: R$ por unidade
   - **Ativo/Inativo**: Habilita/desabilita o serviço

3. Salve - histórico é criado automaticamente

#### ✅ Criar Novo Serviço

1. Clique em "Adicionar Configuração de Serviço Ecossistêmico"
2. Preencha:
   - **Nome**: Ex: "Remoção de NO₂"
   - **Código**: Ex: "poluentes_no2" (slug, único)
   - **Descrição**: Explicação do serviço
   - **Fórmula**: Código Python para cálculo
   - **Coeficientes**: JSON com parâmetros
   - **Valor Monetário**: R$ por unidade
   - **Unidade**: Ex: "g/ano", "ton CO₂"
   - **Categoria**: Sequestro, Interceptação, Energia, Poluição, Outros
   - **Referência Científica**: Citação bibliográfica

3. Salve

#### ✅ Ver Histórico

1. Ao visualizar um serviço, role até "Históricos de Configurações"
2. Veja todas as mudanças com:
   - Usuário que fez a mudança
   - Data/hora
   - Valores anteriores e novos
   - Observações

---

## 📊 Estrutura dos Dados

### Modelo `EcosystemServiceConfig`

```python
{
    'nome': 'Armazenamento de CO₂',
    'codigo': 'co2_armazenado',  # Único, usado para buscar
    'formula': 'math.exp(coeficientes["BETA0"] + ...)',
    'coeficientes': {'BETA0': -0.906586, ...},
    'valor_monetario_unitario': 365.0,
    'unidade_medida': 'ton CO₂',
    'ativo': True,
    'categoria': 'SEQUESTRO',
}
```

### Como Usar no Código

```python
from main.models import Tree, EcosystemServiceConfig

# Obter valor de um serviço específico
tree = Tree.objects.first()
co2 = tree.get_ecosystem_service_value('co2_armazenado')

# Obter todos os serviços ativos
servicos = tree.get_all_ecosystem_services()
# Retorna: {
#   'co2_armazenado': {
#       'nome': 'Armazenamento de CO₂',
#       'valor_fisico': 0.1234,
#       'valor_monetario': 45.01,
#       'unidade': 'ton CO₂',
#       ...
#   },
#   ...
# }
```

---

## ✅ Checklist de Validação

Após implementação, verificar:

- [ ] Migração criada e aplicada com sucesso
- [ ] Serviços iniciais populados (`init_ecosystem_services`)
- [ ] Teste de compatibilidade passou (`test_compatibility`)
- [ ] Admin customizado acessível apenas para gestores
- [ ] É possível criar novos serviços via admin
- [ ] Histórico de mudanças é salvo automaticamente
- [ ] Fórmulas existentes dão resultados idênticos aos métodos antigos
- [ ] Novos serviços (PM2.5, O₃, Absorção Anual) calculam corretamente

---

## 🔧 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'django'"

**Solução**: Ative o ambiente virtual primeiro:
```bash
source venv/bin/activate  # Linux/Mac
```

### Erro ao calcular serviços novos

**Solução**: Verifique se a fórmula usa variáveis corretas:
- `dap` (float)
- `altura` (float)
- `biomassa` (float, em toneladas)
- `tree` (objeto Tree)
- `coeficientes["KEY"]` (acesso aos coeficientes)

### Valores diferentes entre métodos antigos e novos

**Solução**: Execute `test_compatibility` para identificar o problema. Verifique:
1. Se a fórmula está correta
2. Se os coeficientes estão no formato JSON correto
3. Se há diferenças de arredondamento (tolerância: 0.0001)

---

## 📚 Documentação Adicional

- **Metodologias Científicas**: Veja `METODOLOGIAS_SERVICOS_ECOSSISTEMICOS.md`
- **Código dos Modelos**: `habitas/main/models.py`
- **Admin Customizado**: `habitas/main/admin.py`

---

## 🎉 Próximos Passos (Futuro)

- [ ] Interface frontend para exibir novos serviços
- [ ] Dashboard com estatísticas dos novos serviços
- [ ] Exportação de relatórios incluindo novos serviços
- [ ] Integração com dados CETESB em tempo real
- [ ] Taxas variáveis por espécie/idade
- [ ] Mais serviços ecossistêmicos (NO₂, SO₂, etc.)

---

**Sprint 2 - Completa! ✅**

