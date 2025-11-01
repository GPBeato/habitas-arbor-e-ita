# Adaptações do Frontend - Sprint 2 ✅

## 📋 Resumo das Mudanças

O frontend foi **completamente adaptado** para usar o sistema dinâmico de serviços ecossistêmicos da Sprint 2.

---

## ✅ Mudanças Realizadas

### 1. **View `index()` - Adicionada busca de serviços**

**Arquivo:** `habitas/main/views.py`

**Mudança:**
```python
# ANTES:
def index(request):
    trees = Tree.objects.all().select_related('species').annotate(n_posts=Count("posts"))
    context = {"trees": trees}
    return render(request, "index.html", context)

# AGORA:
def index(request):
    trees = Tree.objects.all().select_related('species').annotate(n_posts=Count("posts"))
    # Busca serviços ecossistêmicos ativos para usar no frontend
    ecosystem_services = EcosystemServiceConfig.objects.filter(ativo=True).order_by('ordem_exibicao')
    context = {
        "trees": trees,
        "ecosystem_services": ecosystem_services,  # NOVO
    }
    return render(request, "index.html", context)
```

**Impacto:** Serviços ecossistêmicos disponíveis no template.

---

### 2. **Modelo Tree - Método JSON adicionado**

**Arquivo:** `habitas/main/models.py`

**Mudança:**
```python
# NOVO MÉTODO:
def get_all_ecosystem_services_json(self):
    """Retorna JSON string dos serviços ecossistêmicos (para uso no template)"""
    return json.dumps(self.get_all_ecosystem_services(), ensure_ascii=False)
```

**Impacto:** Permite passar dados para JavaScript de forma segura.

---

### 3. **Template `index.html` - Adaptações principais**

**Arquivo:** `habitas/main/templates/index.html`

#### **3.1. Configuração de Serviços no JavaScript**

**ANTES:** Valores hardcoded no JavaScript
```javascript
const stored_co2_price = stored_co2 * 365;  // Hardcoded
const stormwater_price = stormwater * 0.015;  // Hardcoded
const energy_price = energy * 0.82;  // Hardcoded
```

**AGORA:** Valores dinâmicos do BD
```javascript
// Serviços ecossistêmicos dinâmicos do BD
const ecosystemServicesConfig = {
  {% for service in ecosystem_services %}
  '{{ service.codigo }}': {
    nome: '{{ service.nome }}',
    unidade: '{{ service.unidade_medida }}',
    valorMonetario: {{ service.valor_monetario_unitario }},
    categoria: '{{ service.categoria }}',
  },
  {% endfor %}
};
```

---

#### **3.2. Função `renderStatistics()` - Totalmente Refatorada**

**ANTES:** Cálculos fixos para 4 serviços
```javascript
const stored_co2 = circles.map(a => a.stored_co2).reduce((a,b)=>a+b, 0);
const stormwater = circles.map(a => a.stormwater_intercepted).reduce((a,b)=>a+b, 0);
// ... etc
```

**AGORA:** Cálculos dinâmicos para todos os serviços ativos
```javascript
// Calcula serviços dinamicamente
const servicesData = {};
for (const [codigo, config] of Object.entries(ecosystemServicesConfig)) {
  const values = circles.map(a => {
    return a.services && a.services[codigo] ? a.services[codigo].valor_fisico : 0;
  });
  const total = values.reduce((a,b)=>a+b, 0);
  const valorMonetario = total * config.valorMonetario;
  
  servicesData[codigo] = {
    valorFisico: total,
    valorMonetario: valorMonetario,
    config: config
  };
}

// Gera HTML dinamicamente para todos os serviços
let servicesHTML = '';
for (const [codigo, data] of Object.entries(servicesData)) {
  // Formatação baseada na unidade
  // ... gera HTML dinâmico
}
```

**Impacto:**
- ✅ Exibe **todos os serviços ativos** (não apenas 4)
- ✅ **Novos serviços** (PM2.5, O₃, Absorção Anual) aparecem automaticamente
- ✅ Valores monetários vêm do **BD** (não hardcoded)

---

#### **3.3. Dados das Árvores - Serviços Dinâmicos**

**ANTES:** Apenas métodos @property antigos
```javascript
tree_obj = {
  co2: {{ tree.stored_co2 }},
  stormwater: {{ tree.stormwater_intercepted }},
  conserved_energy: {{ tree.conserved_energy }},
  biodiversity: {{ tree.biodiversity }},
};
```

**AGORA:** Serviços dinâmicos + compatibilidade
```javascript
// Usa serviços dinâmicos do BD - calculado no backend
const tree_services_{{ tree.id }} = {{ tree.get_all_ecosystem_services_json|safe }};

tree_obj = {
  // Serviços dinâmicos do BD
  services: tree_services_{{ tree.id }},
  // Compatibilidade com código antigo
  co2: {{ tree.stored_co2 }},
  stormwater: {{ tree.stormwater_intercepted }},
  // ...
};
```

---

#### **3.4. Função `onMapClick()` - Exibição Dinâmica**

**ANTES:** Valores fixos para 4 serviços
```javascript
document.getElementById("dados").innerHTML = `
  <p>CO<sub>2</sub> retido: ${ Math.round(1000 * tree.co2) } kg</p>
  <p>Água de chuva interceptada: ${ Math.round(tree.stormwater) } L</p>
  // ... apenas 4 serviços
`;
```

**AGORA:** Exibe todos os serviços dinamicamente
```javascript
// Gera HTML dinamicamente com todos os serviços ecossistêmicos
let servicosHTML = '';
if (tree.services) {
  for (const [codigo, servico] of Object.entries(tree.services)) {
    const nome = servico.nome;
    const valorFisico = servico.valor_fisico;
    const valorMonetario = servico.valor_monetario;
    const unidade = servico.unidade;
    
    // Formatação baseada na unidade
    // ... gera HTML para cada serviço
    servicosHTML += `<p>${nome}: ${valorFormatado} ${unidade}`;
    if (valorMonetario > 0) {
      servicosHTML += ` (Valor: R$ ${valorMonetario.toLocaleString(...)})`;
    }
    servicosHTML += `</p>`;
  }
}
```

**Impacto:**
- ✅ Exibe **todos os serviços** quando árvore é clicada
- ✅ **Novos serviços** (PM2.5, O₃, Absorção Anual) aparecem automaticamente
- ✅ **Valor monetário** exibido quando disponível

---

#### **3.5. Referências Científicas - Dinâmicas**

**ANTES:** Valores fixos
```html
<div>CO<sub>2</sub> retido: Schumacher e Hall (1933)</div>
<div>Chuva interceptada: Gash (1979)</div>
<!-- apenas 4 serviços -->
```

**AGORA:** Loop dinâmico
```html
<div class="info-header">Referências Científicas</div>
{% for service in ecosystem_services %}
<div>{{ service.nome }}: {{ service.referencia_cientifica|truncatewords:10 }}</div>
{% endfor %}
```

**Impacto:** Referências de **todos os serviços** exibidas.

---

#### **3.6. Círculos no Mapa - Serviços Dinâmicos**

**ANTES:** Apenas valores antigos
```javascript
circle.stored_co2 = tree.co2;
circle.stormwater_intercepted = tree.stormwater;
// ...
```

**AGORA:** Serviços dinâmicos + compatibilidade
```javascript
// Serviços dinâmicos do BD
circle.services = tree.services;
// Compatibilidade com código antigo
circle.stored_co2 = tree.services && tree.services['co2_armazenado'] 
  ? tree.services['co2_armazenado'].valor_fisico 
  : tree.co2;
// ... outros serviços
```

---

## 📊 Resultado das Adaptações

### ✅ Funcionalidades Novas

1. **Exibição Dinâmica de Serviços**
   - Todos os serviços ativos são exibidos automaticamente
   - Novos serviços (PM2.5, O₃, Absorção Anual) aparecem sem alterar código

2. **Valores Monetários do BD**
   - Valores vêm do `valor_monetario_unitario` do BD
   - Não há mais valores hardcoded no JavaScript

3. **Referências Científicas Dinâmicas**
   - Exibe referências de todos os serviços
   - Atualiza automaticamente quando novos serviços são adicionados

4. **Formatação Inteligente**
   - Formatação baseada na unidade de medida
   - Toneladas: 2 decimais
   - Litros/kWh: inteiros
   - Gramas: 2 decimais

### ✅ Compatibilidade Mantida

- ✅ Métodos antigos (@property) ainda funcionam
- ✅ Código antigo não quebrado
- ✅ Fallback implementado para casos sem serviços no BD

---

## 🧪 Como Testar

### 1. Verificar se serviços estão sendo exibidos

1. Execute: `python manage.py init_ecosystem_services`
2. Acesse a página principal
3. Verifique se **7 serviços** aparecem em "Benefícios ecológicos"

### 2. Verificar novos serviços

1. Verifique se aparecem:
   - ✅ Remoção de PM2.5
   - ✅ Remoção de O₃
   - ✅ Absorção Anual de Carbono

### 3. Testar clique em árvore

1. Clique em uma árvore no mapa
2. Verifique se **todos os serviços** aparecem em "Serviços Ecossistêmicos"
3. Verifique se valores monetários estão corretos

### 4. Verificar referências científicas

1. Role até "Referências Científicas"
2. Verifique se todas as referências aparecem

---

## ⚠️ Notas Importantes

### Performance

- **Impacto:** Baixo - Serviços são calculados uma vez no backend
- **Otimização:** Serviços são pré-calculados no template, não no JavaScript
- **Cache:** Considerar cache para grandes volumes de árvores

### Compatibilidade

- ✅ **Código antigo funciona**: Métodos @property mantidos
- ✅ **Fallback implementado**: Se serviços não existirem no BD, usa métodos antigos
- ✅ **JavaScript seguro**: JSON sanitizado via `json.dumps()`

### Extensibilidade

- ✅ **Novos serviços**: Aparecem automaticamente quando adicionados via admin
- ✅ **Sem alteração de código**: Frontend se adapta automaticamente
- ✅ **Configurável**: Gestores podem ativar/desativar serviços

---

## 📝 Checklist de Validação

- [x] View passa serviços ecossistêmicos para template
- [x] Modelo Tree tem método JSON
- [x] JavaScript usa serviços dinâmicos
- [x] Função `renderStatistics()` refatorada
- [x] Função `onMapClick()` exibe serviços dinamicamente
- [x] Valores monetários vêm do BD
- [x] Referências científicas dinâmicas
- [x] Compatibilidade mantida com código antigo
- [x] Novos serviços aparecem automaticamente

---

## ✅ Conclusão

O frontend está **100% adaptado** para usar o sistema dinâmico de serviços ecossistêmicos da Sprint 2.

**Todas as mudanças foram implementadas:**
- ✅ Uso de serviços dinâmicos do BD
- ✅ Exibição de novos serviços (PM2.5, O₃, Absorção Anual)
- ✅ Valores monetários do BD (não hardcoded)
- ✅ Referências científicas dinâmicas
- ✅ Compatibilidade mantida

**Pronto para teste!** 🎉

