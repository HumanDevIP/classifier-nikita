import pandas as pd
from pandas import DataFrame



def delete_duplicates_in_single_file(dirty_path: str, result_path: str) ->  None:
    """
    Remove duplicate rows from a CSV file based on specified columns and save the cleaned data to a new CSV file.

    This function reads a CSV file, removes duplicate rows based on the 'text' and 'text_b' columns,
    and saves the cleaned data to a new CSV file.

    Arguments:
    - dirty_path (str): The path to the input CSV file that contains potential duplicates.
    - result_path (str): The path where the cleaned CSV file, with duplicates removed, will be saved.

    Return Value:
    - None
    """
    try:
        df: DataFrame = pd.read_csv(dirty_path)
        df_cleaned: DataFrame = df.drop_duplicates(subset=['text', 'text_b'])
        df_cleaned.to_csv(result_path, index=False)
        
    except Exception as e:
        print(f"An error occured during exection 'delete_duplicates_in_single_file' function. Error: {repr(e)}")



delete_duplicates_in_single_file(
    dirty_path='../../data/origin/train.csv',
    result_path='../../data/clean/train_clean.csv'
)