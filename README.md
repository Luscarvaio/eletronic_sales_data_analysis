# Camada de Load

A camada de **Load** é responsável por persistir os dados transformados em formatos de armazenamento analítico.  
Atualmente, o pipeline suporta:

- Exportação para CSV tratado
- Armazenamento em banco analítico DuckDB

Essa camada representa a etapa final do pipeline ETL:

```text
Extract
↓
Transform
↓
Load
```

---

# Objetivo

O objetivo da etapa de Load é:

- Persistir dados limpos e transformados
- Criar datasets reutilizáveis para análise
- Preparar os dados para SQL e ferramentas de BI
- Separar dados brutos de dados processados
- Simular um fluxo ETL utilizado em projetos reais

---

# Destinos de Load

## 1. CSV Processado

O dataset transformado é exportado como um CSV limpo.

### Diretório de saída

```text
data/processed/
```

### Exemplo de arquivo

```text
electronics_sales_clean.csv
```

### Finalidade

- Camada intermediária de armazenamento
- Inspeção e validação dos dados
- Integração com ferramentas externas
- Backup dos dados transformados

---

## 2. DuckDB

O dataset transformado também é carregado em um banco DuckDB.

### Diretório de saída

```text
data/warehouse/
```

### Exemplo de banco

```text
electronics_sales.duckdb
```

### Tabela criada

```sql
sales
```

### Finalidade

- Consultas SQL
- Fluxos analíticos
- Integração com notebooks
- Visualizações em Tableau e ferramentas BI
- Simulação de um Data Warehouse local

---

# Fluxo do Load

```text
DataFrame transformado
↓
Salvar CSV processado
↓
Conectar ao DuckDB
↓
Registrar DataFrame temporário
↓
Criar/Substituir tabela analítica
↓
Fechar conexão
```

---

# Estrutura do Projeto

```text
project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── warehouse/
│
├── src/
│   ├── extract_data.py
│   ├── transform_data.py
│   ├── load_data.py
│
└── main.py
```

---

# Principais Funções

## `load_to_csv()`

Responsável por exportar o DataFrame transformado para um CSV processado.

### Responsabilidades

- Criar diretórios automaticamente
- Persistir o dataset tratado
- Evitar salvar índices desnecessários

---

## `load_to_duckdb()`

Responsável por carregar o DataFrame transformado para o DuckDB.

### Responsabilidades

- Criar diretórios automaticamente
- Abrir conexão com o banco
- Registrar DataFrame temporário
- Criar ou substituir tabela SQL
- Encerrar conexão corretamente

---

# Por que DuckDB?

O DuckDB foi escolhido por ser:

- Leve
- Rápido para análises
- Fácil de integrar com pandas
- Compatível com SQL
- Excelente para projetos analíticos locais
- Muito utilizado em workflows modernos de engenharia de dados

---

# Melhorias Futuras

Possíveis evoluções da camada de Load:

- Incremental Load
- Particionamento de dados
- Sistema de logs
- Validação de schema
- Tratamento avançado de erros
- Configuração via ambiente
- Integração com cloud storage
- Integração com PostgreSQL
- Testes automatizados

---

# Execução do Pipeline

Execute o pipeline com:

```bash
python main.py
```

Saídas esperadas:

```text
data/processed/electronics_sales_clean.csv

data/warehouse/electronics_sales.duckdb
```

---

# Próximos Passos

Após o Load, o projeto estará preparado para:

- Queries SQL analíticas
- Notebooks exploratórios
- Dashboards no Tableau
- Criação de métricas de negócio
- Estudos de modelagem de dados
- Evolução para pipelines mais robustos
