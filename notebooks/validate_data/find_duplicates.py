import pandas as pd
from pandas import DataFrame



def find_duplicates(file_path: str, file_type: str, subset_columns: list[str]) -> None:
    try:
        if file_type == 'parquet':
            df: DataFrame = pd.read_parquet(file_path)
        elif file_type == 'csv':
            df: DataFrame = pd.read_csv(file_path)
        else:
            print("Unsupported type. Use 'parquet' or 'csv'.")
            return

        duplicates: DataFrame = df[df.duplicated(subset=subset_columns, keep=False)]
        
        if not duplicates.empty:
            print(f"There are some duplicates in {file_type.upper()}:")
            print(duplicates)
        else:
            print(f"No duplicates in {file_type.upper()}.")
    
    except Exception as e:
        print(f"An error occured during execution 'find_duplicates' function. Error: {repr(e)}")



file_path_parquet: str = '../../data/clean/test.parquet'
file_path_csv: str = '../../data/clean/test_clean.csv'
subset_columns: list[str] = ['text', 'text_b']

find_duplicates(file_path_parquet, 'parquet', subset_columns)
find_duplicates(file_path_csv, 'csv', subset_columns)
