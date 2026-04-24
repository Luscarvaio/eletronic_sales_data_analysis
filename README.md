# 📊 Sales Data Pipeline & Analysis

## 📌 Overview

Este projeto tem como objetivo construir um fluxo completo de dados (ETL), desde a ingestão de um dataset bruto de vendas até a preparação de uma camada analítica para visualização em BI.

O pipeline inclui:

* Extração de dados (CSV)
* Transformação e limpeza com Python (Pandas)
* Criação de métricas de negócio
* Carregamento em banco analítico (DuckDB)
* Visualização final no Tableau Public

---

## 🎯 Objetivos do Projeto

* Estruturar dados de vendas para análise de negócio
* Identificar padrões de vendas por:

  * Produto
  * Categoria e subcategoria
  * Canal de vendas (online vs físico)
  * Região
  * Representante comercial
* Avaliar relação entre preço e volume de vendas
* Preparar dataset otimizado para ferramentas de BI

---

## 🛠️ Tecnologias Utilizadas

* Python (Pandas)
* DuckDB
* Tableau Public
* Git & GitHub

---

## 📂 Estrutura do Projeto

```
project/
│
├── data/
│   └── electronics_sales_raw.csv
│
├── notebook/
│   └── analysis.ipynb
│
├── output/
│   └── dataset_tratado.csv
│
└── README.md
```

---

## 🔄 Pipeline de Dados

### 1. Extração

* Leitura de dataset CSV contendo dados de vendas, clientes e métricas financeiras

### 2. Transformação

Principais etapas:

* Limpeza de dados (tratamento de strings, datas e valores nulos)
* Conversão de tipos (ex: datas e valores numéricos)
* Criação de colunas derivadas:

  * Ano, mês e trimestre
  * Métrica de receita (`revenue = quantity * unit_price`)
* Padronização de dimensões:

  * Canal de vendas
  * Região
  * Representante
* Agregações para análise

---

### 3. Modelagem Analítica

Criação de dataset consolidado com métricas como:

* Total de pedidos
* Total de unidades vendidas
* Receita total
* Preço médio

Este dataset será utilizado como base para visualização no Tableau.

---

### 4. Load (em desenvolvimento)

Os dados transformados serão carregados em um banco analítico utilizando DuckDB para:

* Melhor performance em consultas
* Simulação de ambiente de dados real

---

### 5. Visualização (em desenvolvimento)

Os dados serão conectados ao Tableau Public para criação de dashboards interativos, incluindo:

* Vendas por canal
* Performance por vendedor
* Receita por categoria
* Análise de preço vs volume

---

## 📈 Principais Métricas

* Total de pedidos
* Receita total
* Quantidade vendida
* Preço médio
* Distribuição por canal e região

---

## 🚧 Status do Projeto

* [x] Extração de dados
* [x] Limpeza inicial
* [x] Feature engineering
* [ ] Criação de métricas avançadas (em andamento)
* [ ] Load em DuckDB
* [ ] Dashboard no Tableau

---

## 📌 Próximos Passos

* Refinar métricas de negócio (ex: ticket médio)
* Implementar carga no DuckDB
* Criar dashboards no Tableau Public
* Adicionar análises mais avançadas (ex: comportamento de clientes e churn)

---

## 💡 Aprendizados

Este projeto foca no desenvolvimento de habilidades práticas em:

* Manipulação e transformação de dados
* Modelagem para análise
* Construção de pipelines de dados
* Preparação de dados para BI

---

## 📬 Contato

Sinta-se à vontade para contribuir ou sugerir melhorias.
