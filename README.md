# Electronic Sales ETL & Analytics Pipeline

Projeto de Engenharia de Dados e Analytics desenvolvido com foco em construção de pipelines ETL, modelagem analítica, métricas de negócio e visualização de dados utilizando Python, DuckDB, SQL e Tableau.

O projeto simula um fluxo moderno de análise de dados, desde a ingestão de arquivos CSV até a criação de métricas analíticas e dashboards.

---

# Objetivo do Projeto

O principal objetivo deste projeto é construir um pipeline ETL completo para:

- Extrair dados de vendas eletrônicas
- Limpar e transformar os dados
- Persistir os dados em um Data Warehouse local
- Criar métricas de negócio
- Construir análises SQL reutilizáveis
- Preparar dados para visualização analítica
- Simular workflows reais de engenharia de dados e analytics engineering

---

# Arquitetura do Projeto

```text
CSV Raw Data
↓
Extract Layer
↓
Transform Layer
↓
Load Layer
↓
DuckDB Warehouse
↓
SQL Analytical Views
↓
Notebook Analysis
↓
Tableau Dashboards
```

---

# Tecnologias Utilizadas

## Linguagens e Ferramentas

- Python
- SQL
- DuckDB
- pandas
- Jupyter Notebook
- Tableau Public
- Git & GitHub

---

# Estrutura do Projeto

```text
etl_eletronic_sales/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── warehouse/
│
├── notebooks/
│   └── eletronic_sales.ipynb
│
├── src/
│   ├── extract_data.py
│   ├── transform_data.py
│   └── load_data.py
│
├── main.py
│
└── README.md
```

---

# Pipeline ETL

## 1. Extract Layer

Responsável pela extração dos dados brutos.

### Funcionalidades

- Leitura de arquivos CSV
- Construção dinâmica de paths utilizando `pathlib`
- Padronização de entrada de dados

---

## 2. Transform Layer

Responsável pelo tratamento e enriquecimento dos dados.

### Transformações realizadas

- Conversão de colunas numéricas
- Conversão de colunas temporais
- Criação de colunas analíticas
- Tratamento de inconsistências
- Criação de métricas financeiras
- Criação de colunas de sazonalidade

---

# Métricas Criadas

## Receita Bruta

```text
gross_revenue = quantity * unit_price
```

---

## Receita Líquida

```text
net_revenue = gross_revenue * (1 - discount_pct)
```

---

## Custo da Mercadoria Vendida

```text
cost_of_goods_sold
```

Criado a partir de regras simuladas por subcategoria.

---

## Lucro Bruto

```text
gross_profit = net_revenue - cost_of_goods_sold
```

---

## Lucro Operacional

```text
operational_profit = gross_profit - monthly_burn
```

---

# Colunas Temporais

A camada de transformação também cria automaticamente:

- mês
- nome do mês
- ano
- trimestre

para colunas temporais do dataset.

---

# 3. Load Layer

Responsável por persistir os dados transformados.

## Destinos

### CSV Processado

```text
data/processed/
```

---

### DuckDB Warehouse

```text
data/warehouse/electronics_sales.duckdb
```

---

# DuckDB

O DuckDB foi utilizado como Data Warehouse analítico local devido a:

- alta performance analítica
- integração com pandas
- suporte SQL
- facilidade de uso local
- integração com notebooks
- compatibilidade com ferramentas analíticas

---

# Camada Analítica

Após o ETL, foram criadas análises SQL utilizando Views.

---

# Views Analíticas

## `top_categories`

Responsável por analisar categorias com melhor desempenho financeiro.

### Métricas

- receita total
- lucro bruto total

---

## `revenue_seasonality`

Responsável pela análise temporal e sazonalidade.

### Métricas

- receita por período
- análise mensal
- tendências temporais

---

# Fluxo Analítico

```text
DuckDB
↓
SQL Views
↓
Notebook Exploration
↓
Tableau Visualization
```

---

# Notebook Analítico

O notebook foi utilizado para:

- exploração analítica
- validação de queries
- testes de métricas
- análises temporais
- desenvolvimento da camada analítica

---

# Conceitos Aplicados

Durante o desenvolvimento foram aplicados conceitos de:

- ETL
- Engenharia de Dados
- Analytics Engineering
- SQL Analítico
- Data Warehouse
- Views SQL
- Modelagem Analítica
- KPIs financeiros
- Sazonalidade
- Métricas de negócio
- Integração pandas + SQL
- Persistência analítica

---

# Principais Aprendizados

O projeto permitiu aprofundar conhecimentos em:

- organização de pipelines ETL
- separação de responsabilidades
- integração entre Python e SQL
- construção de métricas financeiras
- modelagem de dados analíticos
- criação de camadas semânticas
- fluxo moderno de analytics

---

# Próximos Passos

Evoluções planejadas para o projeto:

- criação de dashboards no Tableau
- mais views analíticas
- análise de recorrência de clientes
- KPIs financeiros adicionais
- análise de margem por categoria
- automação de queries
- organização de diretório SQL
- logging estruturado
- testes automatizados
- integração com PostgreSQL
- orquestração futura do pipeline

---

# Como Executar

## Instalar dependências

```bash
pip install pandas duckdb jupyter
```

---

## Executar pipeline

```bash
python main.py
```

---

## Abrir notebook

```bash
jupyter notebook
```

---

# Objetivo Educacional

Este projeto foi desenvolvido com foco em aprendizado prático de:

- engenharia de dados
- pipelines ETL
- SQL analítico
- analytics engineering
- visualização de dados
- workflows modernos de dados
