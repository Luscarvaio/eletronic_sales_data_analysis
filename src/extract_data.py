import pandas as pd
from pathlib import Path

def extract_data(file_name):
    base_dir = Path(__file__).parent.parent
    file_path = base_dir / 'data' / file_name

    if not file_path.is_file():
        raise FileNotFoundError(f'This file does not exist: {file_path}')

    return pd.read_csv(file_path)

df = extract_data('electronics_sales_raw.csv')
print(df.head())

print(df.info())