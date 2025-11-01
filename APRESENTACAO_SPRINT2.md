# 🌳 Sprint 2: Interface Configurável + Novos Serviços Ecossistêmicos
## Sistema Habitas - Gestão de Arborização Urbana

---

## Slide 1: Introdução

**Título:** Apresentação Sprint 2 - Habitas

**Subtítulo:** Sistema de Gestão de Arborização Urbana de São José dos Campos

**Conteúdo:**
- Projeto desenvolvido para quantificação de serviços ecossistêmicos urbanos
- Foco em gestão colaborativa com 3 níveis de usuários (Gestores, Técnicos, Cidadãos)
- ~15.000 árvores cadastradas no sistema

---

## Slide 2: Contexto do Projeto

**Título:** O Problema

**Subtítulo:** Necessidade de gestão inteligente da arborização urbana

**Conteúdo:**
- Quantificação de benefícios ambientais (CO₂, água, energia)
- Gestão participativa envolvendo cidadãos
- Necessidade de sistema configurável para ajustes futuros
- Baseado em modelos científicos reconhecidos

---

## Slide 3: Objetivos da Sprint 2

**Título:** O Que Foi Implementado

**Subtítulo:** Interface Configurável + 2 Novos Serviços Ecossistêmicos

**Conteúdo:**
- ✅ Sistema de configuração dinâmica de serviços ecossistêmicos
- ✅ Interface admin para gestores editarem parâmetros
- ✅ 2 novos serviços: Remoção de Poluentes e Absorção Anual de Carbono
- ✅ Documentação científica completa
- ✅ Migração do banco de dados

---

## Slide 4: Sistema de Configuração Dinâmica (1/3)

**Título:** O Que É Configuração Dinâmica?

**Subtítulo:** Serviços ecossistêmicos configuráveis via banco de dados

**Conteúdo:**
- **Antes**: Cálculos hardcoded no código (não editáveis)
- **Agora**: Cálculos configuráveis via interface admin
- Gestores podem editar fórmulas e coeficientes sem alterar código
- Histórico de todas as mudanças realizadas
- Sistema permite adicionar novos serviços facilmente

---

## Slide 5: Sistema de Configuração Dinâmica (2/3)

**Título:** Componentes do Sistema

**Subtítulo:** Estrutura técnica implementada

**Conteúdo:**
- **Modelo EcosystemServiceConfig**: Armazena configurações de serviços
  - Fórmula Python, coeficientes (JSON), valor monetário
  - Ativo/Inativo, categoria, referência científica
- **Modelo EcosystemServiceHistory**: Histórico de mudanças
  - Quem alterou, quando, valores anteriores e novos
- **Admin Django customizado**: Interface restrita a gestores

---

## Slide 6: Sistema de Configuração Dinâmica (3/3)

**Título:** Funcionalidades da Interface Admin

**Subtítulo:** O que gestores podem fazer

**Conteúdo:**
- ✅ Editar coeficientes dos serviços existentes
- ✅ Modificar fórmulas de cálculo
- ✅ Adicionar novos serviços ecossistêmicos
- ✅ Ativar/desativar serviços
- ✅ Visualizar histórico completo de mudanças
- ✅ Ajustar valoração monetária
- ✅ Acessar referências científicas

---

## Slide 7: Novos Serviços Ecossistêmicos (1/4)

**Título:** A. Remoção de Poluentes

**Subtítulo:** Modelo simplificado baseado em i-Tree

**Conteúdo:**
- **PM2.5** (Partículas finas):
  - Fórmula baseada em biomassa da árvore
  - Taxa de remoção: 0.05 g/m²/ano
  - Concentração média SJC: 20 µg/m³
  - Valoração: R$ 0.50/g (impacto na saúde)
- **O₃** (Ozônio):
  - Taxa de remoção: 0.03 g/m²/ano
  - Concentração média SJC: 100 µg/m³
  - Valoração: R$ 0.45/g (impacto na saúde)

---

## Slide 8: Novos Serviços Ecossistêmicos (2/4)

**Título:** B. Absorção Anual de Carbono

**Subtítulo:** Diferença importante: estoque vs. fluxo

**Conteúdo:**
- **Armazenamento Total**: Carbono acumulado ao longo da vida (estoque)
- **Absorção Anual**: CO₂ sequestrado no ano corrente (fluxo)
- **Fórmula**: Biomassa × Taxa de crescimento (2%) × 0.5
- **Valoração**: R$ 365/ton CO₂/ano
- Diferenciação importante para políticas públicas
- Permite cálculo de benefício anual das árvores

---

## Slide 9: Novos Serviços Ecossistêmicos (3/4)

**Título:** Serviços Existentes (Refatorados)

**Subtítulo:** Cálculos existentes agora configuráveis

**Conteúdo:**
- ✅ **CO₂ Armazenado** (Schumacher & Hall, 1933)
- ✅ **Interceptação de Água Pluvial** (Gash, 1979)
- ✅ **Conservação de Energia** (Ko, 2018)
- ✅ **Índice de Biodiversidade** (proprietário)
- **Todos agora**: Configuráveis via BD, mantendo compatibilidade

---

## Slide 10: Novos Serviços Ecossistêmicos (4/4)

**Título:** Impacto dos Novos Serviços

**Subtítulo:** Quantificação mais completa de benefícios

**Conteúdo:**
- **Antes**: 4 serviços ecossistêmicos
- **Agora**: 7 serviços ecossistêmicos (+3)
- Quantificação de:
  - Impacto na qualidade do ar (PM2.5, O₃)
  - Sequestro anual (diferente de estoque total)
- Valoração monetária mais precisa
- Dados mais completos para tomada de decisão

---

## Slide 11: Documentação Científica (1/2)

**Título:** Metodologias e Referências

**Subtítulo:** Base científica sólida para todos os cálculos

**Conteúdo:**
- **Documento completo**: `METODOLOGIAS_SERVICOS_ECOSSISTEMICOS.md`
- **Fórmulas matemáticas** com notação LaTeX
- **Parâmetros específicos** para São José dos Campos
- **Referências bibliográficas** completas
- **Comparação** com NYC Tree Maps
- **Justificativa** das simplificações adotadas

---

## Slide 12: Documentação Científica (2/2)

**Título:** Modelos Científicos Utilizados

**Subtítulo:** Baseados em literatura reconhecida

**Conteúdo:**
- **Schumacher & Hall (1933)**: Estimativa de biomassa
- **Gash (1979)**: Interceptação de água pluvial
- **Ko (2018)**: Conservação de energia
- **i-Tree Eco v6.0**: Remoção de poluentes (simplificado)
- **Nowak et al. (2013)**: Absorção anual de carbono
- Todos adaptados para contexto regional (SJC)

---

## Slide 13: Implementação Técnica (1/2)

**Título:** Arquitetura da Solução

**Subtítulo:** Componentes implementados

**Conteúdo:**
- **2 Novos Modelos Django**: EcosystemServiceConfig, EcosystemServiceHistory
- **Admin customizado**: Interface restrita a gestores
- **Métodos no modelo Tree**: `get_ecosystem_service_value()`, `get_all_ecosystem_services()`
- **Compatibilidade mantida**: Métodos antigos continuam funcionando
- **Scripts de gerenciamento**: População inicial e testes de compatibilidade

---

## Slide 14: Implementação Técnica (2/2)

**Título:** Migração do Banco de Dados

**Subtítulo:** Estrutura criada

**Conteúdo:**
- **Tabela `main_ecosystemserviceconfig`**: 17 campos
  - Armazena fórmulas, coeficientes, valoração monetária
- **Tabela `main_ecosystemservicehistory`**: 8 campos
  - Histórico completo de mudanças
- **Índices únicos**: Nome e código do serviço
- **Foreign keys**: Relacionamentos com usuários
- **Sem impacto**: Nenhuma tabela existente modificada

---

## Slide 15: Resultados e Validação (1/2)

**Título:** Garantia de Qualidade

**Subtítulo:** Compatibilidade e Testes

**Conteúdo:**
- ✅ **Compatibilidade verificada**: Métodos novos dão resultados idênticos aos antigos
- ✅ **Teste automatizado**: Script `test_compatibility` verifica diferenças
- ✅ **Tolerância**: 0.0001 (valores considerados idênticos)
- ✅ **Fórmulas validadas**: Conforme especificação do README
- ✅ **Código antigo preservado**: Não quebra funcionalidades existentes

---

## Slide 16: Resultados e Validação (2/2)

**Título:** Estatísticas da Implementação

**Subtítulo:** Quantidade de código e funcionalidades

**Conteúdo:**
- **2 novos modelos**: ~130 linhas de código
- **1 admin customizado**: ~100 linhas
- **2 management commands**: ~350 linhas
- **3 novos serviços**: 7 serviços totais no sistema
- **1 documentação científica**: ~370 linhas
- **100% das tarefas concluídas**: Todas as funcionalidades entregues

---

## Slide 17: Impacto Ambiental (1/2)

**Título:** Quantificação de Benefícios

**Subtítulo:** O que as árvores de SJC proporcionam

**Conteúdo:**
- **Armazenamento de CO₂**: Toneladas de carbono estocado
- **Interceptação de água**: Litros/ano reduzindo escoamento
- **Conservação de energia**: kWh/ano economizados
- **Remoção de poluentes**: Gramas/ano de PM2.5 e O₃ removidos
- **Absorção anual**: Toneladas de CO₂ sequestradas por ano
- **Biodiversidade**: Contribuição ao ecossistema local

---

## Slide 18: Impacto Ambiental (2/2)

**Título:** Valoração Monetária

**Subtítulo:** Valor econômico dos serviços ecossistêmicos

**Conteúdo:**
- **CO₂**: R$ 365/ton/ano (mercado de carbono)
- **Água interceptada**: R$ 0.015/L (tratamento de água)
- **Energia conservada**: R$ 0.82/kWh (tarifa elétrica)
- **PM2.5 removido**: R$ 0.50/g (impacto na saúde)
- **O₃ removido**: R$ 0.45/g (impacto na saúde)
- Permite análise custo-benefício de políticas públicas

---

## Slide 19: Comparação com NYC Tree Maps

**Título:** Contextualização Internacional

**Subtítulo:** Inspiração e adaptações

**Conteúdo:**
- **NYC Tree Maps**: Sistema de referência internacional
- **Habitas**: Adaptação para contexto brasileiro (SJC)
- **Simplificações justificadas**: Dados disponíveis limitados
- **Regionalização**: Parâmetros específicos de SJC (clima, poluição)
- **Configurabilidade**: Vantagem do Habitas (NYC não permite edição)

---

## Slide 20: Diferenciais do Sistema

**Título:** O Que Torna o Habitas Único

**Subtítulo:** Inovações implementadas na Sprint 2

**Conteúdo:**
- ✅ **Sistema configurável**: Único sistema que permite editar modelos científicos via interface
- ✅ **Histórico de mudanças**: Auditoria completa de ajustes
- ✅ **Multi-nível**: Gestão colaborativa (Gestores, Técnicos, Cidadãos)
- ✅ **Regionalizado**: Parâmetros específicos de São José dos Campos
- ✅ **Extensível**: Fácil adicionar novos serviços
- ✅ **Transparente**: Documentação científica completa

---

## Slide 21: Casos de Uso

**Título:** Aplicações Práticas

**Subtítulo:** Como gestores podem usar o sistema

**Conteúdo:**
- **Ajuste de parâmetros**: Atualizar coeficientes conforme novos estudos
- **Novos modelos**: Adicionar serviços baseados em pesquisa local
- **Calibração**: Ajustar fórmulas conforme dados coletados
- **Análise de políticas**: Comparar cenários com diferentes parâmetros
- **Educação**: Demonstrar impacto de diferentes espécies
- **Planejamento urbano**: Tomar decisões baseadas em dados

---

## Slide 22: Limitações e Considerações

**Título:** Transparência Científica

**Subtítulo:** Limitações reconhecidas

**Conteúdo:**
- **Simplificações**: Modelos adaptados para dados disponíveis
- **Taxas fixas**: Alguns serviços usam valores médios (ex: crescimento 2%)
- **Estimativas**: Concentrações de poluentes estimadas (não medidas)
- **Dados limitados**: Apenas DAP e altura (sem área foliar específica)
- **Indicativos**: Valores são estimativas, não absolutos
- **Melhorias futuras**: Sistema permite refinamentos sem alterar código

---

## Slide 23: Próximos Passos

**Título:** Evolução Contínua

**Subtítulo:** Melhorias planejadas

**Conteúdo:**
- **Taxas variáveis**: Por espécie e idade (ao invés de fixas)
- **Integração CETESB**: Dados de poluição em tempo real
- **Mais poluentes**: NO₂, SO₂, outros gases
- **Frontend**: Exibir novos serviços no mapa
- **Relatórios**: Exportação incluindo novos serviços
- **Mobile**: App para coleta de dados no campo

---

## Slide 24: Conclusão (1/2)

**Título:** Entregas da Sprint 2

**Subtítulo:** O que foi alcançado

**Conteúdo:**
- ✅ **Sistema configurável**: Interface admin para gestores
- ✅ **3 novos serviços**: PM2.5, O₃, Absorção Anual (+50% de serviços)
- ✅ **Documentação científica**: Completa e referenciada
- ✅ **Migração BD**: Estrutura criada e aplicada
- ✅ **Compatibilidade**: Código antigo preservado
- ✅ **Qualidade**: Testes de compatibilidade implementados

---

## Slide 25: Conclusão (2/2)

**Título:** Impacto do Projeto

**Subtítulo:** Contribuição para sustentabilidade urbana

**Conteúdo:**
- **Gestão inteligente**: Quantificação de benefícios ambientais
- **Tomada de decisão**: Dados para políticas públicas
- **Educação**: Sensibilização sobre valor das árvores urbanas
- **Transparência**: Metodologias científicas documentadas
- **Participação cidadã**: Sistema colaborativo
- **Escalabilidade**: Base sólida para crescimento futuro

---

## Slide 26: Agradecimentos

**Título:** Obrigado!

**Subtítulo:** Habitas - Sistema de Gestão de Arborização Urbana

**Conteúdo:**
- Projeto desenvolvido para São José dos Campos
- Baseado em modelos científicos reconhecidos
- Sistema configurável e extensível
- Contribuindo para cidades mais sustentáveis

**Contato/Dúvidas:**
- Repositório: [GitHub do Habitas]
- Documentação: `METODOLOGIAS_SERVICOS_ECOSSISTEMICOS.md`

---

## Notas para Apresentação

### Dicas:
1. **Slide 1-3**: Contextualização e objetivos (5 min)
2. **Slide 4-6**: Sistema configurável (8 min)
3. **Slide 7-10**: Novos serviços (10 min)
4. **Slide 11-12**: Documentação científica (5 min)
5. **Slide 13-16**: Aspectos técnicos (7 min)
6. **Slide 17-22**: Impacto e aplicações (10 min)
7. **Slide 23-26**: Conclusão (5 min)

**Total estimado**: ~50 minutos (incluindo Q&A)

### Pontos Fortes para Enfatizar:
- **Configurabilidade**: Único sistema que permite editar modelos via interface
- **Base científica**: Todas as metodologias documentadas e referenciadas
- **Aplicação prática**: Dados utilizáveis para políticas públicas
- **Sustentabilidade**: Quantificação de benefícios ambientais reais

