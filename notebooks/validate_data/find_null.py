import pandas as pd
from pandas import DataFrame



def check_null_values(file_path, columns_to_check) -> DataFrame:
    df: DataFrame = pd.read_csv(file_path)
    null_values_in_columns: DataFrame = df[columns_to_check].isnull()
    rows_with_nulls: DataFrame = df[null_values_in_columns.any(axis=1)]
    
    return rows_with_nulls



file_path: str = '../../data/clean/train_clean.csv'
columns_to_check: list[str] = ['text', 'text_b', 'label']

rows_with_nulls: DataFrame = check_null_values(file_path, columns_to_check)
print(rows_with_nulls)