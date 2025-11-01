# 🌳 Sprint 2: Interface Configurável + Novos Serviços Ecossistêmicos
## Habitas - Sistema de Gestão de Arborização Urbana
### Apresentação de 20 minutos

---

## SLIDE 1: TÍTULO

**🌳 Sprint 2: Interface Configurável + Novos Serviços Ecossistêmicos**

Sistema Habitas - Gestão de Arborização Urbana de São José dos Campos

---

## SLIDE 2: CONTEXTO

**O Problema**

• Quantificação de benefícios ambientais das árvores urbanas
• Necessidade de sistema configurável para ajustes futuros
• ~15.000 árvores cadastradas em São José dos Campos
• Baseado em modelos científicos reconhecidos

---

## SLIDE 3: OBJETIVOS

**O Que Foi Implementado**

✅ Sistema de configuração dinâmica de serviços ecossistêmicos
✅ Interface admin para gestores editarem parâmetros
✅ 3 novos serviços: PM2.5, O₃, Absorção Anual de Carbono
✅ Documentação científica completa
✅ Migração do banco de dados

---

## SLIDE 4: CONFIGURAÇÃO DINÂMICA

**O Que É?**

**ANTES:** Cálculos hardcoded no código (não editáveis)

**AGORA:** 
• Gestores podem editar fórmulas e coeficientes via interface
• Histórico de todas as mudanças
• Adicionar novos serviços facilmente

**Vantagem:** Único sistema que permite editar modelos científicos via interface web

---

## SLIDE 5: COMPONENTES TÉCNICOS

**Estrutura Implementada**

**2 Novos Modelos:**
• `EcosystemServiceConfig`: Armazena configurações (fórmula, coeficientes, valoração)
• `EcosystemServiceHistory`: Histórico de mudanças (quem, quando, o que mudou)

**Admin Customizado:**
• Interface restrita a gestores e superusers
• Edição completa de serviços ecossistêmicos

---

## SLIDE 6: NOVOS SERVIÇOS - POLUENTES

**Remoção de Poluentes (i-Tree simplificado)**

**PM2.5:**
• Taxa: 0.05 g/m²/ano
• Concentração SJC: 20 µg/m³
• Valoração: R$ 0.50/g

**O₃:**
• Taxa: 0.03 g/m²/ano
• Concentração SJC: 100 µg/m³
• Valoração: R$ 0.45/g

**Impacto:** Quantificação do benefício para qualidade do ar

---

## SLIDE 7: NOVOS SERVIÇOS - ABSORÇÃO ANUAL

**Absorção Anual de Carbono**

**Conceito:**
• **Armazenamento Total** = Carbono acumulado (estoque)
• **Absorção Anual** = CO₂ sequestrado no ano (fluxo)

**Fórmula:**
• Biomassa × Taxa crescimento (2%) × 0.5

**Valoração:** R$ 365/ton CO₂/ano

**Importância:** Permite calcular benefício anual vs. total acumulado

---

## SLIDE 8: SERVIÇOS EXISTENTES

**Agora Configuráveis via BD**

✅ CO₂ Armazenado (Schumacher & Hall, 1933)
✅ Interceptação Água Pluvial (Gash, 1979)
✅ Conservação de Energia (Ko, 2018)
✅ Índice de Biodiversidade

**Resultado:** 
• Antes: 4 serviços fixos
• Agora: 7 serviços configuráveis (+3 novos)

---

## SLIDE 9: DOCUMENTAÇÃO CIENTÍFICA

**Base Científica Sólida**

• Fórmulas matemáticas com notação LaTeX
• Parâmetros específicos para São José dos Campos
• Referências bibliográficas completas
• Comparação com NYC Tree Maps
• Justificativa das simplificações

**Modelos Utilizados:**
• Schumacher & Hall (1933), Gash (1979), Ko (2018)
• i-Tree Eco v6.0, Nowak et al. (2013)

---

## SLIDE 10: IMPLEMENTAÇÃO TÉCNICA

**Arquitetura**

**Banco de Dados:**
• 2 novas tabelas criadas
• Nenhuma tabela existente modificada
• Compatibilidade total mantida

**Código:**
• 2 novos modelos Django
• Admin customizado (~100 linhas)
• Scripts de gerenciamento
• Testes de compatibilidade

**Resultado:** 100% das tarefas concluídas

---

## SLIDE 11: GARANTIA DE QUALIDADE

**Compatibilidade e Testes**

✅ Métodos novos dão resultados idênticos aos antigos
✅ Teste automatizado verifica diferenças (tolerância: 0.0001)
✅ Fórmulas validadas conforme especificação
✅ Código antigo preservado (não quebra funcionalidades)

**Qualidade:** Sistema testado e validado

---

## SLIDE 12: IMPACTO AMBIENTAL

**Quantificação de Benefícios**

**Serviços Quantificados:**
• Armazenamento de CO₂ (toneladas)
• Interceptação de água (litros/ano)
• Conservação de energia (kWh/ano)
• Remoção de poluentes (g/ano de PM2.5 e O₃)
• Absorção anual de CO₂ (ton/ano)

**Valoração Monetária:**
• Permite análise custo-benefício para políticas públicas

---

## SLIDE 13: DIFERENCIAIS

**O Que Torna o Habitas Único**

✅ **Configurável**: Editar modelos científicos via interface (único no mercado)
✅ **Transparente**: Documentação científica completa
✅ **Regionalizado**: Parâmetros específicos de SJC
✅ **Colaborativo**: 3 níveis de usuários (Gestores, Técnicos, Cidadãos)
✅ **Extensível**: Fácil adicionar novos serviços

---

## SLIDE 14: CASOS DE USO

**Aplicações Práticas**

**Gestores podem:**
• Ajustar parâmetros conforme novos estudos
• Adicionar serviços baseados em pesquisa local
• Calibrar fórmulas com dados coletados
• Comparar cenários com diferentes parâmetros
• Tomar decisões baseadas em dados quantificados

**Resultado:** Gestão mais inteligente da arborização urbana

---

## SLIDE 15: LIMITAÇÕES

**Transparência Científica**

**Reconhecidas:**
• Simplificações adaptadas para dados disponíveis
• Taxas fixas (médias, não por espécie)
• Estimativas de concentrações (não medidas)
• Valores são indicativos, não absolutos

**Melhorias futuras:** Sistema permite refinamentos sem alterar código

---

## SLIDE 16: CONCLUSÃO

**Entregas da Sprint 2**

✅ Sistema configurável completo
✅ 3 novos serviços (+50% de serviços)
✅ Documentação científica completa
✅ Migração BD aplicada
✅ Compatibilidade mantida

**Impacto:** Gestão inteligente e quantificada da arborização urbana

---

## SLIDE 17: PRÓXIMOS PASSOS

**Evolução Contínua**

• Taxas variáveis por espécie e idade
• Integração com dados CETESB em tempo real
• Mais poluentes (NO₂, SO₂)
• Relatórios com exportação completa

**Base sólida:** Sistema extensível para crescimento futuro

---

## SLIDE 18: AGRADECIMENTOS

**🌳 Habitas - Contribuindo para Cidades Mais Sustentáveis**

Projeto desenvolvido para São José dos Campos

**Baseado em modelos científicos reconhecidos**
**Sistema configurável e extensível**
**Gestão inteligente da arborização urbana**

**Obrigado!**

---

# GUIA DE APRESENTAÇÃO - 20 MINUTOS

## Timing Sugerido:

| Seção | Slides | Tempo |
|-------|--------|-------|
| Introdução | 1-2 | 2 min |
| Objetivos | 3 | 1 min |
| Sistema Configurável | 4-5 | 3 min |
| Novos Serviços | 6-8 | 5 min |
| Aspectos Técnicos | 9-11 | 3 min |
| Impacto e Aplicações | 12-15 | 4 min |
| Conclusão | 16-18 | 2 min |

**Total:** 18 slides em 20 minutos (incluindo transições)

## Dicas:

• **Foque nos diferenciais**: Sistema configurável é único
• **Enfatize impacto**: Quantificação de benefícios ambientais
• **Mantenha ritmo**: ~1 minuto por slide
• **Seja objetivo**: Evite detalhes técnicos excessivos
• **Deixe tempo para Q&A**: Reserve 2-3 minutos no final

## Pontos Fortes para Enfatizar:

1. **Configurabilidade** = Único sistema que permite editar modelos via interface
2. **Base científica** = Metodologias documentadas e referenciadas
3. **Aplicação prática** = Dados utilizáveis para políticas públicas
4. **Sustentabilidade** = Quantificação real de benefícios ambientais

