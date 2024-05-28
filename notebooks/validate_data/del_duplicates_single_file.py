import pandas as pd
from pandas import DataFrame



def delete_duplicates_in_single_file(dirty_path: str, result_path: str) ->  None:
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