# Metodologias de Cálculo de Serviços Ecossistêmicos

## 🌳 Habitas - Sistema de Gestão de Arborização Urbana

Este documento descreve as metodologias científicas utilizadas para calcular os serviços ecossistêmicos das árvores urbanas no sistema Habitas.

---

## 1. Armazenamento de CO₂ (Schumacher & Hall, 1933)

### Fórmula

$$\ln{C} = \beta_0 + \beta_1 \ln{DAP} + \beta_2 \ln{H_t}$$

Onde:
- **C** = Carbono armazenado (kg)
- **DAP** = Diâmetro à Altura do Peito (cm)
- **H_t** = Altura total da árvore (m)

### Parâmetros

```
β₀ = -0.906586 
β₁ = 1.60421 
β₂ = 0.37162
```

### Implementação

```python
C = exp(β₀ + β₁ * ln(DAP) + β₂ * ln(H_t)) / 1000  # Converte kg para toneladas
```

### Valoração Monetária

- **R$ 365/ton CO₂/ano** (baseado em mercado de carbono brasileiro)
- Fonte: Preços médios de carbono em 2023-2024

### Referência

Schumacher, F. X., & Hall, F. C. (1933). Logarithmic expression of timber-tree volume. *Journal of Agricultural Research*, 47(9), 719-734.

---

## 2. Interceptação de Água Pluvial (Gash, 1979)

### Fórmula

$$I = \pi \times \left(\frac{DAP \times R}{2 \times 100}\right)^2 \times P$$

Onde:
- **I** = Interceptação anual (L/ano)
- **R** = Razão diâmetro copa/tronco = 4 (média para espécies urbanas)
- **P** = Precipitação anual = 1329 L/m²/ano (São José dos Campos)

### Parâmetros Específicos de SJC

- Precipitação média anual: ~1329 mm = 1329 L/m²
- Dados: INMET (Instituto Nacional de Meteorologia)

### Implementação

```python
area_copa = π * (raio_copa)²
raio_copa = (DAP * RATIO) / (2 * 100)  # em metros
I = area_copa * PRECIPITATION
```

### Valoração Monetária

- **R$ 0.015/L** (custo médio de tratamento de água)
- Baseado em custos operacionais de estações de tratamento

### Referência

Gash, J. H. C. (1979). An analytical model of rainfall interception by forests. *Quarterly Journal of the Royal Meteorological Society*, 105(443), 43-55.

---

## 3. Conservação de Energia (Ko, 2018)

### Fórmula

$$E = \pi \times \left(\frac{DAP \times R}{2 \times 100}\right)^2 \times R_{sol} \times \eta$$

Onde:
- **E** = Energia conservada (kWh/ano)
- **R_{sol}** = Radiação solar anual = 1661 kWh/m²/ano (SJC)
- **η** = Taxa de aproveitamento da sombra = 0.25 (25%)

### Parâmetros Específicos de SJC

- Radiação solar média anual: ~1661 kWh/m²
- Taxa de aproveitamento: 25% (estimativa conservadora)
- Dados: INMET

### Implementação

```python
area_sombreamento = π * (raio_copa)²
E = area_sombreamento * RADIATION * ENERGY_RATIO
```

### Valoração Monetária

- **R$ 0.82/kWh** (tarifa média de energia elétrica residencial em SJC)
- Fonte: ANEEL (Agência Nacional de Energia Elétrica)

### Referência

Ko, Y. (2018). Trees and vegetation for residential energy conservation: A critical review for evidence-based urban greening in North America. *Urban Forestry & Urban Greening*, 34, 318-335.

---

## 4. Índice de Biodiversidade

### Descrição

Cálculo proprietário baseado em múltiplos fatores:

- **Diversidade de espécies**: Contribuição relativa à diversidade local
- **Potencial de abrigo para fauna**: Estrutura da copa e tronco
- **Produção de frutos/flores**: Recursos alimentares
- **Contribuição ao ecossistema local**: Interações ecológicas

### Implementação

Valor atribuído por espécie (`Species.bio_index`):

```python
biodiversidade = species.bio_index if species else 1.0
```

### Escala

- **1.0** = Valor base (espécie comum)
- **> 1.0** = Maior contribuição à biodiversidade
- Valores típicos: 1.0 - 3.0

### Valoração Monetária

- **Sem valoração monetária padrão** (índice qualitativo)

### Referência

Estimativa própria baseada em literatura sobre serviços ecossistêmicos de árvores urbanas.

---

## 5. Remoção de Poluentes - PM2.5 (Simplificado i-Tree)

### Fórmula

$$R_{PM2.5} = 0.0001 \times B \times \tau_{PM2.5} \times C_{PM2.5}$$

Onde:
- **R_{PM2.5}** = Remoção anual de PM2.5 (g/ano)
- **B** = Biomassa (ton)
- **τ_{PM2.5}** = Taxa de remoção = 0.05 g/m² de área foliar/ano
- **C_{PM2.5}** = Concentração média = 20 µg/m³ (estimado SJC)

### Parâmetros

- Taxa de remoção: 0.05 g/m²/ano (i-Tree simplificado)
- Concentração PM2.5: 20 µg/m³ (estimativa para SJC)
- Fonte: CETESB e simplificação de modelos i-Tree

### Implementação

```python
biomassa = exp(β₀ + β₁ * ln(DAP) + β₂ * ln(H_t)) / 1000  # toneladas
R_PM25 = 0.0001 * biomassa * TAXA_REMOCAO_PM25 * CONCENTRACAO_PM25
```

### Valoração Monetária

- **R$ 0.50/g PM2.5** (estimado impacto na saúde)
- Baseado em estudos de impacto econômico da poluição do ar

### Referência

i-Tree Eco v6.0. US Forest Service. Simplified model for PM2.5 removal.

---

## 6. Remoção de Poluentes - O₃ (Simplificado i-Tree)

### Fórmula

$$R_{O3} = 0.0001 \times B \times \tau_{O3} \times C_{O3}$$

Onde:
- **R_{O3}** = Remoção anual de ozônio (g/ano)
- **B** = Biomassa (ton)
- **τ_{O3}** = Taxa de remoção = 0.03 g/m²/ano
- **C_{O3}** = Concentração média = 100 µg/m³ (estimado SJC)

### Parâmetros

- Taxa de remoção: 0.03 g/m²/ano (i-Tree simplificado)
- Concentração O₃: 100 µg/m³ (estimativa para SJC)

### Valoração Monetária

- **R$ 0.45/g O₃** (estimado impacto na saúde)

### Referência

i-Tree Eco v6.0. US Forest Service. Simplified model for O₃ removal.

---

## 7. Absorção Anual de Carbono

### Fórmula

$$A_{anual} = B \times \tau_{cresc} \times 0.5$$

Onde:
- **A_{anual}** = Absorção anual de CO₂ (ton CO₂/ano)
- **B** = Biomassa atual (ton)
- **τ_{cresc}** = Taxa de crescimento anual = 2%
- **0.5** = Proporção de carbono na biomassa seca

### Diferença do Armazenamento Total

| Conceito | Descrição |
|----------|-----------|
| **Armazenamento Total** | Carbono acumulado ao longo da vida da árvore |
| **Absorção Anual** | Quantidade de CO₂ sequestrada no ano corrente |

### Parâmetros

- Taxa de crescimento anual: 2% (taxa fixa simplificada)
- Proporção carbono: 50% da biomassa seca (padrão científico)

### Implementação

```python
biomassa = exp(β₀ + β₁ * ln(DAP) + β₂ * ln(H_t)) / 1000  # toneladas
absorcao_anual = biomassa * TAXA_CRESCIMENTO_ANUAL * 0.5
```

### Valoração Monetária

- **R$ 365/ton CO₂/ano** (mesma do armazenamento)

### Referência

Modelo simplificado baseado em taxas de crescimento anual médio. Adaptado de Nowak et al. (2013). Carbon storage and sequestration by trees.

---

## Comparação com NYC Tree Maps

| Serviço | NYC Tree Maps | Habitas | Justificativa da Diferença |
|---------|---------------|---------|---------------------------|
| **CO₂ Armazenado** | i-Tree Eco completo | Schumacher & Hall (1933) | Modelo mais simples, adequado ao contexto regional e dados disponíveis |
| **Interceptação** | Modelo Gash completo | Gash simplificado | Abordagem pragmática para MVP, mantendo base científica |
| **Energia** | Modelo detalhado com clima | Ko (2018) simplificado | Boa aproximação considerando dados climáticos locais |
| **Poluentes** | i-Tree completo | Versão simplificada | Adequado para MVP, permite refinamento futuro |
| **Absorção Anual** | Não calculado separadamente | Novo serviço | Diferenciação importante entre estoque e fluxo |
| **Biodiversidade** | Não calculado | Índice próprio | Adaptação às necessidades locais |

---

## Justificativa das Simplificações

### 1. Dados Disponíveis Limitados

O sistema atual dispõe apenas de:
- DAP (Diâmetro à Altura do Peito)
- Altura total
- Espécie (para alguns registros)

Não dispomos de:
- Área foliar específica
- Dados climáticos detalhados
- Medições de crescimento
- Análises de solo

**Solução**: Modelos simplificados que utilizam DAP e altura como proxies.

### 2. Região Específica (São José dos Campos)

- **Clima**: Subtropical úmido
- **Precipitação**: ~1329 mm/ano
- **Radiação solar**: ~1661 kWh/m²/ano
- **Concentrações de poluentes**: Estimadas baseadas em CETESB

**Solução**: Parâmetros calibrados especificamente para SJC.

### 3. MVP Pragmático

Foco em:
- ✅ Funcionalidade antes de precisão absoluta
- ✅ Transparência nas metodologias
- ✅ Facilidade de ajuste futuro

**Solução**: Sistema configurável via admin permite refinamentos sem alteração de código.

### 4. Configurabilidade

O sistema permite:
- Ajuste de coeficientes via admin
- Adição de novos serviços
- Modificação de fórmulas
- Histórico de mudanças

---

## Limitações e Considerações

### Limitações Atuais

1. **Taxas fixas**: Alguns serviços usam taxas fixas (ex: crescimento anual 2%)
   - **Solução futura**: Taxas variáveis por espécie/idade

2. **Simplificações**: Modelos simplificados podem subestimar/superestimar valores reais
   - **Mitigação**: Valores são indicativos, não absolutos

3. **Concentrações de poluentes**: Estimadas, não medidas
   - **Solução futura**: Integração com dados CETESB em tempo real

### Considerações

- Os valores calculados são **estimativas** baseadas em modelos científicos
- Devem ser usados para **comparações relativas** entre árvores
- Não substituem análises técnicas detalhadas
- Podem variar conforme condições locais

---

## Referências Bibliográficas Completas

1. **Schumacher, F. X., & Hall, F. C.** (1933). Logarithmic expression of timber-tree volume. *Journal of Agricultural Research*, 47(9), 719-734.

2. **Gash, J. H. C.** (1979). An analytical model of rainfall interception by forests. *Quarterly Journal of the Royal Meteorological Society*, 105(443), 43-55.

3. **Ko, Y.** (2018). Trees and vegetation for residential energy conservation: A critical review for evidence-based urban greening in North America. *Urban Forestry & Urban Greening*, 34, 318-335.

4. **Nowak, D. J., et al.** (2013). Carbon storage and sequestration by trees in urban and community areas of the United States. *Environmental Pollution*, 178, 229-236.

5. **i-Tree Eco v6.0 Documentation.** US Forest Service. Disponível em: https://www.itreetools.org/

6. **CETESB** - Companhia Ambiental do Estado de São Paulo. Dados de qualidade do ar.

7. **INMET** - Instituto Nacional de Meteorologia. Dados climáticos.

8. **ANEEL** - Agência Nacional de Energia Elétrica. Tarifas de energia.

---

## Contato e Contribuições

Para dúvidas sobre metodologias ou sugestões de melhorias:

- **Repositório**: [GitHub do Habitas]
- **Issues**: Reportar através do GitHub

---

**Versão do Documento**: 1.0  
**Data**: 2024  
**Última Atualização**: Sprint 2 - Sistema Configurável

