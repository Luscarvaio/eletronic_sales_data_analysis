from pathlib import Path
import pandas as pd 
import duckdb 

def load_to_csv(df, output_file='electronics_sales_transformed.csv'):
    # definindo o caminho do arquivo de saída
    base_dir = Path(__file__).parent.parent 

    # criando o caminho completo para o arquivo de saída
    output_path = (
        base_dir 
        / 'data' 
        / 'processed'
        / output_file
    )

    # criando o diretório se ele não existir
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # transformando o DataFrame em CSV e salvando no caminho definido
    df.to_csv(output_path, index=False)

    # verificando se o arquivo foi salvo corretamente
    print(f'CSV file saved successfully at: {output_path}')

def load_to_duckdb(
    df,
    db_name='electronics_sales.duckdb',
    table_name='sales'
):
    base_dir = Path(__file__).parent.parent

    db_path = (
        base_dir 
        / 'data' 
        / 'warehouse' 
        / db_name
    )
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = duckdb.connect(str(db_path))

    conn.register('temp_df', df) 

    conn.execute(f"""
    CREATE OR REPLACE TABLE {table_name} AS
    SELECT *
    FROM temp_df
    """)
    conn.close()

    print(f'DuckDB table "{table_name}" created successfully in database: {db_path}')

def load_data(df):

    load_to_csv(df)

    load_to_duckdb(df)

    print('Load completed successfully.')