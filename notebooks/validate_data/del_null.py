import pandas as pd
from pandas import DataFrame



def remove_null_values(file_path: str, columns_to_check: list[str]) -> None:
    try:
        df: DataFrame = pd.read_csv(file_path)
        df_cleaned: DataFrame = df.dropna(subset=columns_to_check)
        df_cleaned.to_csv(file_path, index=False)
    
    except Exception as e:
        print(f"An error occured during exection 'remove_null_values' function. Error: {repr(e)}")



file_path: str = '../../data/work_data/train_work.csv'
columns_to_check: list[str] = ['text', 'text_b', 'label']

remove_null_values(file_path, columns_to_check)