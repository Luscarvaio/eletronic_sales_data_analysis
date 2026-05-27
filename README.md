````markdown
# Camada Analítica e Views SQL

Após a construção das etapas de Extract, Transform e Load, o projeto passou a incluir uma camada analítica baseada em SQL utilizando DuckDB.

Essa etapa tem como objetivo transformar os dados já tratados em métricas de negócio reutilizáveis para análises, dashboards e exploração analítica.

Fluxo atual do projeto:

```text
CSV bruto
↓
ETL Python
↓
DuckDB Warehouse
↓
Views SQL Analíticas
↓
Notebook / Tableau
```

---

# Objetivo

A camada analítica foi criada para:

- Centralizar métricas de negócio
- Evitar duplicação de lógica no Tableau
- Facilitar análises exploratórias
- Criar uma camada semântica reutilizável
- Melhorar organização do projeto analítico
- Simular workflows reais de analytics engineering

---

# Arquitetura Analítica

## Tabela Base

```text
sales
```

Tabela criada pelo pipeline ETL contendo:

- Dados tratados
- Colunas temporais
- Métricas financeiras
- KPIs derivados

---

# Views Criadas

## 1. `top_categories`

View responsável por identificar categorias com melhor desempenho financeiro.

### Métricas calculadas

- Receita total por categoria
- Lucro bruto total por categoria

### Query

```sql
CREATE OR REPLACE VIEW top_categories AS

SELECT
    category,
    SUM(net_revenue) AS total_revenue,
    SUM(gross_profit) AS total_gross_profit
FROM sales
GROUP BY category
```

---

# Objetivo Analítico

Essa view permite:

- Identificar categorias mais lucrativas
- Comparar desempenho entre categorias
- Criar rankings financeiros
- Analisar concentração de receita

---

## 2. `revenue_seasonality`

View responsável pela análise temporal e sazonalidade de receita.

### Métrica calculada

- Receita total por período

### Query

```sql
CREATE OR REPLACE VIEW revenue_seasonality AS

SELECT
    order_date_year,
    order_date_month,
    order_date_month_name,
    SUM(net_revenue) AS total_revenue
FROM sales
GROUP BY
    order_date_year,
    order_date_month,
    order_date_month_name
```

---

# Objetivo Analítico

Essa view permite:

- Identificar sazonalidade
- Detectar picos e quedas de receita
- Comparar desempenho mensal
- Construir análises temporais no Tableau

---

# Estrutura Atual

```text
project/
│
├── data/
│   └── warehouse/
│       └── electronics_sales.duckdb
│
├── notebooks/
│   └── eletronic_sales.ipynb
│
├── src/
│   ├── extract_data.py
│   ├── transform_data.py
│   └── load_data.py
│
└── main.py
```

---

# Fluxo de Desenvolvimento Analítico

O fluxo utilizado no projeto segue:

```text
Notebook
↓
Criação e validação de queries
↓
Transformação em Views SQL
↓
Consumo no Tableau
```

---

# Tecnologias Utilizadas

- Python
- pandas
- DuckDB
- SQL
- Jupyter Notebook
- Tableau

---

# Benefícios da Utilização de Views

A utilização de Views SQL permite:

- Centralizar regras analíticas
- Evitar lógica duplicada no dashboard
- Melhorar manutenção do projeto
- Facilitar reutilização de métricas
- Separar visualização da lógica de negócio

---

# Próximos Passos

Possíveis evoluções futuras:

- Views de recorrência de clientes
- KPIs financeiros mensais
- Análise de margem por categoria
- Ticket médio por período
- Dashboards interativos no Tableau
- Camada semântica mais robusta
- Queries SQL organizadas em diretório próprio
- Automação das views no pipeline ETL

---

# Conceitos Trabalhados

Durante essa etapa foram aplicados conceitos de:

- SQL analítico
- Data Warehouse
- Views SQL
- Métricas financeiras
- Sazonalidade
- Analytics Engineering
- Modelagem analítica
- Camada semântica de dados
````
