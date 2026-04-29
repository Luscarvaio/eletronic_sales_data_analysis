# 📊 Sales Data Pipeline & Analysis

## 📌 Overview

Este projeto tem como objetivo construir um fluxo completo de dados (ETL), desde a ingestão de um dataset bruto de vendas até a preparação de uma camada analítica para visualização em BI.

Inicialmente desenvolvido em notebook para exploração, o projeto foi evoluído para scripts Python organizados em módulos (`extract`, `transform`), visando maior reprodutibilidade, organização e alinhamento com boas práticas de engenharia de dados.

O pipeline inclui:

* Extração de dados (CSV)
* Transformação e limpeza com Python (Pandas)
* Criação de métricas de negócio
* Carregamento em banco analítico (DuckDB)
* Visualização final no Tableau Public

---

## 🎯 Objetivos do Projeto

* Estruturar dados de vendas para análise de negócio
* Aplicar boas práticas de transformação e tratamento de dados
* Identificar padrões de vendas por:
  * Produto
  * Categoria e subcategoria
  * Canal de vendas
  * Região
  * Representante comercial
* Criar métricas relevantes para tomada de decisão
* Preparar dataset para consumo em ferramentas de BI

---

## 🛠️ Tecnologias Utilizadas

* Python (Pandas)
* DuckDB (em desenvolvimento)
* Tableau Public (em desenvolvimento)
* Git & GitHub

---

## 📂 Estrutura do Projeto

project/
│
├── src/
│   ├── extract_data.py
│   └── transform_data.py
│
├── data/
│   └── electronics_sales_raw.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── output/
│   └── dataset_tratado.csv
│
└── README.md
---

## 🔄 Pipeline de Dados

## 🔄 Pipeline de Dados

### 1. Extração (`extract`)

A etapa de extração foi implementada em script Python, substituindo a leitura direta em notebook.

Principais responsabilidades:

* Leitura do dataset CSV bruto
* Padronização inicial do carregamento
* Retorno de um DataFrame reutilizável para o pipeline

Essa abordagem permite maior reutilização, organização e manutenção do código.

---

### 2. Transformação (`transform`)

A transformação foi estruturada em funções modulares, aproximando o projeto de um pipeline real de dados.

Principais etapas:

#### ✔️ Limpeza e Conversão de Tipos

* Conversão de colunas numéricas (`unit_price`, `quantity`, etc.)
* Tratamento de inconsistências (ex: separadores, valores inválidos)

#### ✔️ Tratamento de Datas

* Conversão para datetime
* Tratamento de erros (`errors='coerce'`)

#### ✔️ Feature Engineering

* Criação da métrica de receita:

revenue = quantity * unit_price


* Criação de colunas temporais:
* Ano
* Mês
* Trimestre

#### ✔️ Padronização

* Normalização de dimensões (canal, região, vendedor)
* Organização dos dados para consumo analítico

---

### 3. Modelagem Analítica

Criação de um dataset consolidado com métricas como:

* Total de pedidos
* Quantidade vendida
* Receita total
* Preço médio

Este dataset serve como base para análises e dashboards.

---

### 4. Load (em desenvolvimento)

Os dados transformados serão carregados em um banco analítico utilizando DuckDB, permitindo:

* Execução de queries SQL
* Melhor performance analítica
* Simulação de ambiente real de dados

---

### 5. Análise e Visualização (em desenvolvimento)

A análise será dividida em duas camadas:

* **Jupyter Notebook** → exploração e geração de insights
* **Tableau Public** → construção de dashboards interativos

Principais análises previstas:

* Receita por canal
* Performance por vendedor
* Receita por categoria
* Relação entre preço e volume

---

## 🔁 Evolução do Projeto

O projeto passou por duas fases principais:

### Fase 1 — Exploração

* Uso de notebook para análise inicial
* Testes de transformação

### Fase 2 — Estruturação

* Migração para scripts Python
* Separação em módulos (`extract` e `transform`)
* Aplicação de boas práticas de engenharia de dados

Essa evolução reflete a transição de um ambiente exploratório para um pipeline mais próximo de produção.

---

## 📈 Principais Métricas

* Receita total (`Revenue`)
* Quantidade vendida
* Preço médio
* Total de pedidos
* Dimensões temporais (ano, mês, trimestre)

---

## 🚧 Status do Projeto

* [x] Extração de dados
* [x] Limpeza e transformação
* [x] Feature engineering
* [ ] Criação de métricas avançadas (em andamento)
* [ ] Load em DuckDB
* [ ] Dashboard no Tableau

---

## 📌 Próximos Passos

* Implementar etapa de Load com DuckDB
* Criar camada analítica consolidada
* Refinar métricas de negócio (ex: ticket médio)
* Desenvolver dashboards no Tableau Public
* Gerar insights de negócio a partir dos dados
* Adicionar análises mais avançadas (ex: comportamento de clientes e churn)

---

## 💡 Aprendizados

* Estruturação de pipelines ETL
* Modularização de código em Python
* Tratamento e transformação de dados com Pandas
* Modelagem de dados para análise
* Diferença entre análise exploratória e código produtivo
* Preparação de dados para ferramentas de BI

---

## 📬 Contato

Sinta-se à vontade para contribuir ou sugerir melhorias.
