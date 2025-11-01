# APRESENTAÇÃO SPRINT 2 - HABITAS

---

## SLIDE 1: TÍTULO

**🌳 Sprint 2: Interface Configurável + Novos Serviços Ecossistêmicos**

Sistema Habitas - Gestão de Arborização Urbana

---

## SLIDE 2: INTRODUÇÃO

**Contexto do Projeto**

• Projeto desenvolvido para quantificação de serviços ecossistêmicos urbanos
• Foco em gestão colaborativa com 3 níveis de usuários
• ~15.000 árvores cadastradas no sistema
• Baseado em modelos científicos reconhecidos internacionalmente

---

## SLIDE 3: O PROBLEMA

**Necessidade de Gestão Inteligente da Arborização Urbana**

• Quantificação de benefícios ambientais (CO₂, água, energia)
• Gestão participativa envolvendo cidadãos
• Necessidade de sistema configurável para ajustes futuros
• Baseado em modelos científicos reconhecidos

---

## SLIDE 4: OBJETIVOS DA SPRINT 2

**O Que Foi Implementado**

✅ Sistema de configuração dinâmica de serviços ecossistêmicos
✅ Interface admin para gestores editarem parâmetros
✅ 2 novos serviços: Remoção de Poluentes e Absorção Anual de Carbono
✅ Documentação científica completa
✅ Migração do banco de dados

---

## SLIDE 5: CONFIGURAÇÃO DINÂMICA - CONCEITO

**O Que É Configuração Dinâmica?**

**ANTES:**
• Cálculos hardcoded no código (não editáveis)
• Alterações requeriam programador

**AGORA:**
• Cálculos configuráveis via interface admin
• Gestores podem editar fórmulas e coeficientes sem alterar código
• Histórico de todas as mudanças realizadas
• Sistema permite adicionar novos serviços facilmente

---

## SLIDE 6: COMPONENTES DO SISTEMA

**Estrutura Técnica Implementada**

**Modelo EcosystemServiceConfig:**
• Armazena configurações de serviços
• Fórmula Python, coeficientes (JSON), valor monetário
• Ativo/Inativo, categoria, referência científica

**Modelo EcosystemServiceHistory:**
• Histórico de mudanças
• Quem alterou, quando, valores anteriores e novos

**Admin Django customizado:**
• Interface restrita a gestores

---

## SLIDE 7: FUNCIONALIDADES DA INTERFACE

**O Que Gestores Podem Fazer**

✅ Editar coeficientes dos serviços existentes
✅ Modificar fórmulas de cálculo
✅ Adicionar novos serviços ecossistêmicos
✅ Ativar/desativar serviços
✅ Visualizar histórico completo de mudanças
✅ Ajustar valoração monetária
✅ Acessar referências científicas

---

## SLIDE 8: NOVOS SERVIÇOS - POLUENTES (PM2.5)

**Remoção de PM2.5 - Partículas Finas**

**Modelo:**
• Baseado em i-Tree simplificado
• Fórmula baseada em biomassa da árvore
• Taxa de remoção: 0.05 g/m²/ano
• Concentração média SJC: 20 µg/m³

**Valoração:**
• R$ 0.50/g (impacto na saúde)

---

## SLIDE 9: NOVOS SERVIÇOS - POLUENTES (O₃)

**Remoção de O₃ - Ozônio**

**Modelo:**
• Baseado em i-Tree simplificado
• Taxa de remoção: 0.03 g/m²/ano
• Concentração média SJC: 100 µg/m³

**Valoração:**
• R$ 0.45/g (impacto na saúde)

---

## SLIDE 10: NOVOS SERVIÇOS - ABSORÇÃO ANUAL

**Absorção Anual de Carbono**

**Conceito Importante:**
• **Armazenamento Total**: Carbono acumulado ao longo da vida (estoque)
• **Absorção Anual**: CO₂ sequestrado no ano corrente (fluxo)

**Fórmula:**
• Biomassa × Taxa de crescimento (2%) × 0.5

**Valoração:**
• R$ 365/ton CO₂/ano

---

## SLIDE 11: SERVIÇOS EXISTENTES REFATORADOS

**Cálculos Existentes Agora Configuráveis**

✅ **CO₂ Armazenado** (Schumacher & Hall, 1933)
✅ **Interceptação de Água Pluvial** (Gash, 1979)
✅ **Conservação de Energia** (Ko, 2018)
✅ **Índice de Biodiversidade** (proprietário)

**Todos agora:** Configuráveis via BD, mantendo compatibilidade

---

## SLIDE 12: IMPACTO DOS NOVOS SERVIÇOS

**Quantificação Mais Completa de Benefícios**

**Antes:** 4 serviços ecossistêmicos
**Agora:** 7 serviços ecossistêmicos (+3)

**Quantificação de:**
• Impacto na qualidade do ar (PM2.5, O₃)
• Sequestro anual (diferente de estoque total)

**Resultado:**
• Valoração monetária mais precisa
• Dados mais completos para tomada de decisão

---

## SLIDE 13: DOCUMENTAÇÃO CIENTÍFICA

**Metodologias e Referências**

• **Documento completo**: `METODOLOGIAS_SERVICOS_ECOSSISTEMICOS.md`
• **Fórmulas matemáticas** com notação LaTeX
• **Parâmetros específicos** para São José dos Campos
• **Referências bibliográficas** completas
• **Comparação** com NYC Tree Maps
• **Justificativa** das simplificações adotadas

---

## SLIDE 14: MODELOS CIENTÍFICOS UTILIZADOS

**Baseados em Literatura Reconhecida**

• **Schumacher & Hall (1933)**: Estimativa de biomassa
• **Gash (1979)**: Interceptação de água pluvial
• **Ko (2018)**: Conservação de energia
• **i-Tree Eco v6.0**: Remoção de poluentes (simplificado)
• **Nowak et al. (2013)**: Absorção anual de carbono

**Todos adaptados para contexto regional (SJC)**

---

## SLIDE 15: ARQUITETURA DA SOLUÇÃO

**Componentes Implementados**

• **2 Novos Modelos Django**: EcosystemServiceConfig, EcosystemServiceHistory
• **Admin customizado**: Interface restrita a gestores
• **Métodos no modelo Tree**: Cálculos dinâmicos
• **Compatibilidade mantida**: Métodos antigos continuam funcionando
• **Scripts de gerenciamento**: População inicial e testes

---

## SLIDE 16: MIGRAÇÃO DO BANCO DE DADOS

**Estrutura Criada**

**Tabela `main_ecosystemserviceconfig`:** 17 campos
• Armazena fórmulas, coeficientes, valoração monetária

**Tabela `main_ecosystemservicehistory`:** 8 campos
• Histórico completo de mudanças

**Resultado:**
• Índices únicos: Nome e código do serviço
• Foreign keys: Relacionamentos com usuários
• **Sem impacto**: Nenhuma tabela existente modificada

---

## SLIDE 17: GARANTIA DE QUALIDADE

**Compatibilidade e Testes**

✅ **Compatibilidade verificada**: Métodos novos dão resultados idênticos aos antigos
✅ **Teste automatizado**: Script verifica diferenças
✅ **Tolerância**: 0.0001 (valores considerados idênticos)
✅ **Fórmulas validadas**: Conforme especificação do README
✅ **Código antigo preservado**: Não quebra funcionalidades existentes

---

## SLIDE 18: ESTATÍSTICAS DA IMPLEMENTAÇÃO

**Quantidade de Código e Funcionalidades**

• **2 novos modelos**: ~130 linhas de código
• **1 admin customizado**: ~100 linhas
• **2 management commands**: ~350 linhas
• **3 novos serviços**: 7 serviços totais no sistema
• **1 documentação científica**: ~370 linhas
• **100% das tarefas concluídas**: Todas as funcionalidades entregues

---

## SLIDE 19: QUANTIFICAÇÃO DE BENEFÍCIOS

**O Que as Árvores de SJC Proporcionam**

• **Armazenamento de CO₂**: Toneladas de carbono estocado
• **Interceptação de água**: Litros/ano reduzindo escoamento
• **Conservação de energia**: kWh/ano economizados
• **Remoção de poluentes**: Gramas/ano de PM2.5 e O₃ removidos
• **Absorção anual**: Toneladas de CO₂ sequestradas por ano
• **Biodiversidade**: Contribuição ao ecossistema local

---

## SLIDE 20: VALORAÇÃO MONETÁRIA

**Valor Econômico dos Serviços Ecossistêmicos**

• **CO₂**: R$ 365/ton/ano (mercado de carbono)
• **Água interceptada**: R$ 0.015/L (tratamento de água)
• **Energia conservada**: R$ 0.82/kWh (tarifa elétrica)
• **PM2.5 removido**: R$ 0.50/g (impacto na saúde)
• **O₃ removido**: R$ 0.45/g (impacto na saúde)

**Permite análise custo-benefício de políticas públicas**

---

## SLIDE 21: COMPARAÇÃO COM NYC TREE MAPS

**Contextualização Internacional**

**NYC Tree Maps:**
• Sistema de referência internacional

**Habitas:**
• Adaptação para contexto brasileiro (SJC)
• Simplificações justificadas (dados limitados)
• Regionalização: Parâmetros específicos de SJC
• **Configurabilidade**: Vantagem do Habitas (NYC não permite edição)

---

## SLIDE 22: DIFERENCIAIS DO SISTEMA

**O Que Torna o Habitas Único**

✅ **Sistema configurável**: Único sistema que permite editar modelos científicos via interface
✅ **Histórico de mudanças**: Auditoria completa de ajustes
✅ **Multi-nível**: Gestão colaborativa (Gestores, Técnicos, Cidadãos)
✅ **Regionalizado**: Parâmetros específicos de São José dos Campos
✅ **Extensível**: Fácil adicionar novos serviços
✅ **Transparente**: Documentação científica completa

---

## SLIDE 23: CASOS DE USO

**Aplicações Práticas**

**Como gestores podem usar o sistema:**

• **Ajuste de parâmetros**: Atualizar coeficientes conforme novos estudos
• **Novos modelos**: Adicionar serviços baseados em pesquisa local
• **Calibração**: Ajustar fórmulas conforme dados coletados
• **Análise de políticas**: Comparar cenários com diferentes parâmetros
• **Educação**: Demonstrar impacto de diferentes espécies
• **Planejamento urbano**: Tomar decisões baseadas em dados

---

## SLIDE 24: LIMITAÇÕES E CONSIDERAÇÕES

**Transparência Científica**

**Limitações reconhecidas:**

• **Simplificações**: Modelos adaptados para dados disponíveis
• **Taxas fixas**: Alguns serviços usam valores médios (ex: crescimento 2%)
• **Estimativas**: Concentrações de poluentes estimadas (não medidas)
• **Dados limitados**: Apenas DAP e altura (sem área foliar específica)
• **Indicativos**: Valores são estimativas, não absolutos
• **Melhorias futuras**: Sistema permite refinamentos sem alterar código

---

## SLIDE 25: PRÓXIMOS PASSOS

**Evolução Contínua**

**Melhorias planejadas:**

• **Taxas variáveis**: Por espécie e idade (ao invés de fixas)
• **Integração CETESB**: Dados de poluição em tempo real
• **Mais poluentes**: NO₂, SO₂, outros gases
• **Frontend**: Exibir novos serviços no mapa
• **Relatórios**: Exportação incluindo novos serviços
• **Mobile**: App para coleta de dados no campo

---

## SLIDE 26: CONCLUSÃO - ENTREGAS

**O Que Foi Alcançado**

✅ **Sistema configurável**: Interface admin para gestores
✅ **3 novos serviços**: PM2.5, O₃, Absorção Anual (+50% de serviços)
✅ **Documentação científica**: Completa e referenciada
✅ **Migração BD**: Estrutura criada e aplicada
✅ **Compatibilidade**: Código antigo preservado
✅ **Qualidade**: Testes de compatibilidade implementados

---

## SLIDE 27: CONCLUSÃO - IMPACTO

**Contribuição para Sustentabilidade Urbana**

• **Gestão inteligente**: Quantificação de benefícios ambientais
• **Tomada de decisão**: Dados para políticas públicas
• **Educação**: Sensibilização sobre valor das árvores urbanas
• **Transparência**: Metodologias científicas documentadas
• **Participação cidadã**: Sistema colaborativo
• **Escalabilidade**: Base sólida para crescimento futuro

---

## SLIDE 28: AGRADECIMENTOS

**🌳 Habitas - Sistema de Gestão de Arborização Urbana**

Projeto desenvolvido para São José dos Campos

**Baseado em modelos científicos reconhecidos**
**Sistema configurável e extensível**
**Contribuindo para cidades mais sustentáveis**

**Contato/Dúvidas:**
• Repositório: [GitHub do Habitas]
• Documentação: `METODOLOGIAS_SERVICOS_ECOSSISTEMICOS.md`

---

# DICAS PARA APRESENTAÇÃO

## Estrutura Temporal Recomendada:

1. **Slide 1-4**: Contextualização e objetivos (5 min)
2. **Slide 5-7**: Sistema configurável (8 min)
3. **Slide 8-12**: Novos serviços (10 min)
4. **Slide 13-14**: Documentação científica (5 min)
5. **Slide 15-18**: Aspectos técnicos (7 min)
6. **Slide 19-24**: Impacto e aplicações (10 min)
7. **Slide 25-28**: Conclusão (5 min)

**Total estimado**: ~50 minutos (incluindo Q&A)

## Pontos Fortes para Enfatizar:

• **Configurabilidade**: Único sistema que permite editar modelos via interface
• **Base científica**: Todas as metodologias documentadas e referenciadas
• **Aplicação prática**: Dados utilizáveis para políticas públicas
• **Sustentabilidade**: Quantificação de benefícios ambientais reais

## Visual Sugerido:

• Use cores verdes para temas ambientais
• Gráficos/infográficos para serviços ecossistêmicos
• Screenshots do admin para demonstração
• Comparações visuais (antes/depois, quantidade de serviços)

