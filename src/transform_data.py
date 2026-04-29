from extract_data import extract_data
import pandas as pd 
from pathlib import Path 

df = extract_data('electronics_sales_raw.csv')
columns_to_convert_float = ['unit_price', 'quantity', 'monthly_burn', 'debt_balance', 'cash_balance']
date_columns = ['order_date', 'first_purchase_date', 'last_purchase_date']

def convert_to_float(df, columns):
    for col in columns:
        if col in df.columns:
            df[col] = (
                df[col].astype(str)
                .str.replace(',', '', regex=False)
            )
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def create_revenue_column(df, price_col, quantity_col=None):
    if price_col not in df.columns:
        raise ValueError(f'Price column "{price_col}" does not exist in the DataFrame.')
    
    if quantity_col and quantity_col in df.columns:
        df['Revenue'] = df[price_col] * df[quantity_col]
    else:
        df['Revenue'] = df[price_col]
    return df

def convert_to_datetime(df, columns):
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        else:
            raise ValueError(f'Date column "{col}" does not exist in the DataFrame.')
    return df

def create_month_year_quarter_columns(df, date_columns):
    meses = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março',
        4: 'Abril', 5: 'Maio', 6: 'Junho',
        7: 'Julho', 8: 'Agosto', 9: 'Setembro',
        10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    for col in date_columns:  
        if col not in df.columns:
            raise ValueError(f'Date column "{col}" does not exist in the DataFrame.')
        
        df[f'{col}_month'] = df[col].dt.month
        df[f'{col}_month_name'] = df[f'{col}_month'].map(meses)
        df[f'{col}_year'] = df[col].dt.year
        df[f'{col}_quarter'] = df[col].dt.quarter

        return df

def data_transformation(df):
    df = convert_to_float(df, columns_to_convert_float)
    df = create_revenue_column(df, 'unit_price', 'quantity')
    df = convert_to_datetime(df, date_columns)
    df = create_month_year_quarter_columns(df, date_columns)
    return df

df = data_transformation(df)
print(df.info())
print(df['order_date_month_name'].head())






