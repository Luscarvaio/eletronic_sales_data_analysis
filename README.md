# Camada de Transform

A camada de **Transform** é responsável por limpar, padronizar, enriquecer e preparar os dados para análise.  
Essa etapa representa o núcleo do pipeline ETL, onde os dados brutos passam por regras de negócio e tratamento de inconsistências.

O fluxo atual segue:

```text
Extract
↓
Transform
↓
Load
```

---

# Objetivo

A etapa de Transform tem como finalidade:

- Corrigir inconsistências nos dados
- Padronizar tipos de dados
- Criar métricas derivadas
- Preparar colunas temporais para análise
- Garantir maior qualidade dos dados
- Tornar o dataset pronto para SQL e ferramentas analíticas

---

# Principais Transformações

## 1. Conversão de Valores Numéricos

Função:

```python
convert_to_float()
```

### Objetivo

Converter colunas numéricas que chegam como texto para formato numérico adequado.

### Tratamentos realizados

- Conversão para string
- Remoção de separadores inválidos
- Conversão para valores numéricos
- Tratamento de erros com `errors='coerce'`

### Exemplo

Antes:

```text
"1,200"
```

Depois:

```text
1200.0
```

---

# Colunas Numéricas Tratadas

```python
columns_to_convert_float = [
    'unit_price',
    'quantity',
    'monthly_burn',
    'debt_balance',
    'cash_balance'
]
```

---

# 2. Criação da Coluna Revenue

Função:

```python
create_revenue_column()
```

### Objetivo

Criar uma métrica de faturamento baseada no preço unitário e quantidade.

### Regra aplicada

```text
Revenue = unit_price × quantity
```

### Comportamento

- Valida se a coluna de preço existe
- Verifica se a coluna de quantidade foi informada
- Calcula faturamento automaticamente

### Exemplo

| unit_price | quantity | Revenue |
|---|---|---|
| 100 | 2 | 200 |

---

# 3. Conversão de Datas

Função:

```python
convert_to_datetime()
```

### Objetivo

Padronizar colunas temporais para o formato datetime do pandas.

### Tratamentos realizados

- Conversão para datetime
- Tratamento de valores inválidos
- Coerção de erros com `errors='coerce'`

### Colunas Tratadas

```python
date_columns = [
    'order_date',
    'first_purchase_date',
    'last_purchase_date'
]
```

---

# 4. Criação de Colunas Temporais

Função:

```python
create_month_year_quarter_columns()
```

### Objetivo

Criar colunas auxiliares para análises temporais.

### Colunas criadas automaticamente

Para cada coluna de data:

- Mês numérico
- Nome do mês
- Ano
- Trimestre

### Exemplo

Para:

```text
order_date
```

São geradas:

```text
order_date_month
order_date_month_name
order_date_year
order_date_quarter
```

---

# Fluxo da Camada de Transform

```text
DataFrame bruto
↓
Conversão de valores numéricos
↓
Criação da coluna Revenue
↓
Conversão de datas
↓
Criação de colunas temporais
↓
DataFrame analítico tratado
```

---

# Estrutura Atual

```text
src/
└── transform_data.py
```

---

# Função Principal

A função principal da camada de transformação é:

```python
data_transformation()
```

Ela centraliza todas as etapas de limpeza e enriquecimento do dataset.

### Fluxo interno

```python
convert_to_float()
↓
create_revenue_column()
↓
convert_to_datetime()
↓
create_month_year_quarter_columns()
```

---

# Tratamento de Erros

O pipeline utiliza validações para evitar falhas silenciosas.

Exemplos:

- Verificação de existência de colunas
- Validação de colunas temporais
- Tratamento de conversões inválidas
- Uso de `ValueError` para erros críticos

---

# Objetivo Analítico

Após a transformação, o dataset fica preparado para:

- Queries SQL
- Dashboards
- KPIs
- Análises temporais
- Análise de faturamento
- Segmentações de negócio
- Integração com Tableau
- Estudos exploratórios em notebooks

---

# Melhorias Futuras

Possíveis evoluções da camada de Transform:

- Padronização de schema
- Logging estruturado
- Tratamento de valores ausentes
- Validação de tipos
- Criação de métricas adicionais
- Pipeline incremental
- Testes automatizados
- Configuração via arquivo `.env`
- Uso de classes para organização do pipeline

---

# Execução

A transformação é executada automaticamente no pipeline principal:

```bash
python main.py
```

Fluxo completo:

```text
Extract
↓
Transform
↓
Load
```
