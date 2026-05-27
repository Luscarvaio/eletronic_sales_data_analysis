from src.extract_data import extract_data
from src.transform_data import data_transformation
from src.load_data import load_data


def main():
    df = extract_data("electronics_sales_raw.csv")
    
    df = data_transformation(df)
    
    load_data(df)


if __name__ == "__main__":
    main()
    
