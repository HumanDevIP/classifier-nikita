import pandas as pd
from pandas import DataFrame



def check_null_values(file_path: str, columns_to_check: list[str]) -> DataFrame:
    """
    Identify rows with null values in specified columns of a CSV file.

    This function reads a CSV file, checks the specified columns for null values,
    and returns a DataFrame containing the rows that have null values in any of the specified columns.

    Arguments:
    - file_path (str): The path to the input CSV file.
    - columns_to_check (list[str]): A list of column names to check for null values.

    Return Value:
    - rows_with_nulls (DataFrame): A Pandas DataFrame containing the rows that have null values in any of the specified columns.
    """
    df: DataFrame = pd.read_csv(file_path)
    null_values_in_columns: DataFrame = df[columns_to_check].isnull()
    rows_with_nulls: DataFrame = df[null_values_in_columns.any(axis=1)]
    
    return rows_with_nulls



file_path: str = '../../data/clean/train_clean.csv'
columns_to_check: list[str] = ['text', 'text_b', 'label']

rows_with_nulls: DataFrame = check_null_values(file_path, columns_to_check)
print(rows_with_nulls)