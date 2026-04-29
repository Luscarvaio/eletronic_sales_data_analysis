# 📊 Sales Data Pipeline & Analysis

## 📌 Overview

Projeto de pipeline de dados para análise de vendas, com foco na construção de um fluxo ETL estruturado e aplicação de boas práticas de engenharia de dados.

Inicialmente desenvolvido em notebook para exploração, o projeto foi evoluído para scripts Python organizados em módulos (`extract`, `transform`), visando maior reprodutibilidade, organização e alinhamento com cenários reais de desenvolvimento.

---

## 🎯 Objetivos do Projeto

* Estruturar dados de vendas para análise de negócio
* Aplicar boas práticas de transformação e tratamento de dados
* Criar métricas relevantes para tomada de decisão
* Preparar dataset para consumo em ferramentas de BI

---

## 🛠️ Tecnologias Utilizadas

* Python (Pandas)
* DuckDB *(em desenvolvimento)*
* Tableau Public *(em desenvolvimento)*
* Git & GitHub

---

## 📂 Estrutura do Projeto

```
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
│
├── output/
│
└── README.md
```

---

## 🔄 Pipeline de Dados

### 1. Extração (`extract`)

A etapa de extração foi implementada em script Python, substituindo a leitura direta em notebook.

Principais responsabilidades:

* Leitura do dataset CSV bruto
* Padronização inicial do carregamento
* Retorno de um DataFrame reutilizável para o pipeline

Essa separação permite:

* Reutilização do código
* Facilidade de manutenção
* Melhor organização do fluxo de dados

---

### 2. Transformação (`transform`)

A transformação foi estruturada em funções modulares, permitindo maior clareza e escalabilidade.

Principais etapas implementadas:

#### ✔️ Conversão de tipos

* Conversão de colunas numéricas (`unit_price`, `quantity`, etc.)
* Tratamento de inconsistências em valores (ex: separadores)

#### ✔️ Tratamento de datas

* Conversão de colunas para datetime
* Tratamento de valores inválidos (`errors='coerce'`)

#### ✔️ Feature Engineering

* Criação da métrica de receita:

  ```
  revenue = quantity * unit_price
  ```

* Criação de colunas temporais:

  * Ano
  * Mês
  * Trimestre

#### ✔️ Padronização

* Organização de colunas para facilitar análise posterior
* Preparação dos dados para consumo em BI

---

## 🔁 Evolução do Projeto

O projeto passou por duas fases:

### Fase 1 — Exploração

* Uso de notebook para análise inicial
* Testes de transformação

### Fase 2 — Estruturação

* Migração para scripts Python
* Separação em módulos (`extract` e `transform`)
* Aplicação de boas práticas de engenharia de dados

Essa evolução reflete a transição de um ambiente exploratório para um pipeline mais próximo de produção.

---

## 📈 Métricas Criadas

* Receita total (`Revenue`)
* Quantidade vendida
* Preço unitário tratado
* Dimensões temporais (ano, mês, trimestre)

---

## 🚧 Status do Projeto

* [x] Extração de dados
* [x] Limpeza e transformação
* [x] Feature engineering
* [ ] Load em DuckDB
* [ ] Dashboard no Tableau

---

## 📌 Próximos Passos

* Implementar etapa de Load com DuckDB
* Criar camada analítica consolidada
* Desenvolver dashboards no Tableau
* Gerar insights de negócio a partir dos dados

---

## 💡 Aprendizados

* Estruturação de pipelines ETL
* Modularização de código em Python
* Tratamento e transformação de dados com Pandas
* Diferença entre análise exploratória e código produtivo

---

## 📬 Contato

Sinta-se à vontade para contribuir ou sugerir melhorias.
