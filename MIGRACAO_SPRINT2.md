# Migração do Banco de Dados - Sprint 2 ✅

## 📋 Resumo das Mudanças

A migração `0002_add_ecosystem_services.py` foi **criada e aplicada com sucesso**.

---

## 🗄️ Estrutura das Novas Tabelas

### 1. Tabela: `main_ecosystemserviceconfig`

**Propósito**: Armazena configurações dinâmicas de serviços ecossistêmicos.

**Campos Criados**:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | BigAutoField | Chave primária |
| `nome` | CharField(255) | Nome do serviço (único) |
| `codigo` | SlugField(100) | Código único do serviço (único, slug) |
| `descricao` | TextField | Descrição do serviço |
| `formula` | TextField | Fórmula Python para cálculo |
| `coeficientes` | JSONField | Coeficientes da fórmula (JSON) |
| `valor_monetario_unitario` | FloatField | Valor monetário por unidade (R$) |
| `unidade_medida` | CharField(50) | Unidade de medida |
| `ativo` | BooleanField | Serviço ativo/inativo |
| `ordem_exibicao` | IntegerField | Ordem de exibição |
| `referencia_cientifica` | CharField(500) | Referência científica |
| `categoria` | CharField(50) | Categoria (SEQUESTRO, INTERCEPTACAO, ENERGIA, POLUICAO, OUTROS) |
| `data_criacao` | DateTimeField | Data de criação (auto) |
| `data_atualizacao` | DateTimeField | Data de atualização (auto) |
| `criado_por_id` | ForeignKey | Referência ao usuário que criou (SET_NULL) |

**Índices**:
- `nome` (único)
- `codigo` (único)
- `ordem_exibicao` + `nome` (ordenação)

### 2. Tabela: `main_ecosystemservicehistory`

**Propósito**: Armazena histórico de mudanças nas configurações de serviços.

**Campos Criados**:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | BigAutoField | Chave primária |
| `acao` | CharField(255) | Ação realizada |
| `valores_anteriores` | JSONField | Valores anteriores (JSON) |
| `valores_novos` | JSONField | Valores novos (JSON) |
| `observacao` | TextField | Observação |
| `data` | DateTimeField | Data da mudança (auto) |
| `servico_id` | ForeignKey | Referência ao serviço (CASCADE) |
| `usuario_id` | ForeignKey | Referência ao usuário (CASCADE) |

**Índices**:
- `-data` (ordenação decrescente)
- Foreign keys: `servico_id`, `usuario_id`

---

## 🔗 Relacionamentos Criados

1. **EcosystemServiceConfig → CustomUser**
   - Campo: `criado_por`
   - Tipo: ForeignKey (SET_NULL)
   - Related name: `servicos_criados`

2. **EcosystemServiceHistory → EcosystemServiceConfig**
   - Campo: `servico`
   - Tipo: ForeignKey (CASCADE)
   - Related name: `historico`

3. **EcosystemServiceHistory → CustomUser**
   - Campo: `usuario`
   - Tipo: ForeignKey (CASCADE)
   - Related name: (padrão)

---

## ✅ Status da Migração

```
Migrations for 'main':
  main/migrations/0002_add_ecosystem_services.py
    - Create model EcosystemServiceConfig
    - Create model EcosystemServiceHistory

Operations to perform:
  Apply all migrations: main
Running migrations:
  Applying main.0002_add_ecosystem_services... OK
```

**✅ Migração aplicada com sucesso!**

---

## 📊 Impacto no Banco de Dados

### Tabelas Existentes
- ✅ **Nenhuma tabela existente foi modificada**
- ✅ **Compatibilidade total mantida**
- ✅ **Dados existentes preservados**

### Novas Tabelas
- ✅ `main_ecosystemserviceconfig` criada
- ✅ `main_ecosystemservicehistory` criada

### Tamanho Estimado

Para um sistema com ~15.000 árvores:
- **EcosystemServiceConfig**: ~7 registros (serviços iniciais) ≈ 10-20 KB
- **EcosystemServiceHistory**: Cresce conforme mudanças, ~100-500 registros ≈ 50-200 KB

**Total**: ~60-220 KB (muito leve)

---

## 🎯 Próximos Passos

### 1. Popular Serviços Iniciais

```bash
cd habitas
python manage.py init_ecosystem_services
```

Isso criará 7 serviços:
1. Armazenamento de CO₂
2. Interceptação de Água Pluvial
3. Conservação de Energia
4. Índice de Biodiversidade
5. Remoção de PM2.5 (NOVO)
6. Remoção de O₃ (NOVO)
7. Absorção Anual de Carbono (NOVO)

### 2. Testar Compatibilidade

```bash
python manage.py test_compatibility
```

Verifica se os cálculos novos são idênticos aos antigos.

### 3. Verificar no Admin

1. Acesse `/admin/` como gestor
2. Veja "Configurações de Serviços Ecossistêmicos"
3. Verifique se os 7 serviços foram criados

---

## 🔍 Verificação do Banco de Dados

### SQL para Verificar (SQLite)

```sql
-- Verificar se tabelas foram criadas
SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%ecosystem%';

-- Contar serviços criados
SELECT COUNT(*) FROM main_ecosystemserviceconfig;

-- Ver serviços criados
SELECT nome, codigo, ativo, categoria FROM main_ecosystemserviceconfig ORDER BY ordem_exibicao;

-- Ver histórico (após primeira mudança)
SELECT COUNT(*) FROM main_ecosystemservicehistory;
```

### Django Shell

```python
from main.models import EcosystemServiceConfig, EcosystemServiceHistory

# Verificar serviços
servicos = EcosystemServiceConfig.objects.all()
print(f"Total de serviços: {servicos.count()}")

# Ver histórico
historico = EcosystemServiceHistory.objects.all()
print(f"Total de histórico: {historico.count()}")
```

---

## ⚠️ Notas Importantes

1. **Sem Dados Perdidos**: A migração não modifica tabelas existentes
2. **Compatibilidade**: Código antigo continua funcionando
3. **Rollback**: Migração pode ser revertida com `python manage.py migrate main 0001`
4. **Backup**: Recomendado fazer backup antes de migrações em produção

---

## 📝 Arquivo de Migração Criado

**Localização**: `habitas/main/migrations/0002_add_ecosystem_services.py`

**Dependências**: 
- `main.0001_initial` (migração inicial)

**Operações**:
1. Criar modelo `EcosystemServiceConfig`
2. Criar modelo `EcosystemServiceHistory`

---

## ✅ Conclusão

A migração foi **criada e aplicada com sucesso**. O banco de dados agora possui as tabelas necessárias para o sistema de configuração dinâmica de serviços ecossistêmicos.

**Status**: ✅ **COMPLETO**

---

**Data da Migração**: 2025-11-01  
**Django Version**: 4.1.2  
**App**: main

