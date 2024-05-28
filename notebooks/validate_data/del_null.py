import pandas as pd
from pandas import DataFrame



def remove_null_values(file_path: str, columns_to_check: list[str]) -> None:
    df: DataFrame = pd.read_csv(file_path)
    df_cleaned: DataFrame = df.dropna(subset=columns_to_check)
    df_cleaned.to_csv(file_path, index=False)



file_path: str = '../../data/clean/train_clean.csv'
columns_to_check: list[str] = ['text', 'text_b']

remove_null_values(file_path, columns_to_check)