import pandas as pd
from pandas import DataFrame



def remove_null_values(file_path: str, columns_to_check: list[str]) -> None:
    """
    Remove rows with null values in specified columns from a CSV file.

    This function reads a CSV file, removes rows that contain null values in any of the specified columns,
    and saves the cleaned data back to the same CSV file.

    Arguments:
    - file_path (str): The path to the input CSV file.
    - columns_to_check (list[str]): A list of column names to check for null values. Rows with null values in any of these columns will be removed.

    Return Value:
    - None
    """
    try:
        df: DataFrame = pd.read_csv(file_path)
        df_cleaned: DataFrame = df.dropna(subset=columns_to_check)
        df_cleaned.to_csv(file_path, index=False)
    
    except Exception as e:
        print(f"An error occured during exection 'remove_null_values' function. Error: {repr(e)}")



file_path: str = '../../data/clean/train_clean.csv'
columns_to_check: list[str] = ['text', 'text_b', 'label']

remove_null_values(file_path, columns_to_check)