import pandas as pd
from pandas import DataFrame



def delete_duplicates_cross_files(filepath_1: str, filepath_2: str) -> None:
    try:
        df1: DataFrame = pd.read_csv(filepath_1)
        df2: DataFrame = pd.read_csv(filepath_2)

        duplicates = df1.merge(df2, how='inner')

        df1_cleaned: DataFrame = df1[~df1.index.isin(duplicates.index)]

        df1_cleaned.to_csv(filepath_1, index=False)
        df2.to_csv(filepath_2, index=False)

        print("Duplicate records successfully removed")
    
    except Exception as e:
        print(f"An error occured during exection 'delete_duplicates_cross_files' function. Error: {repr(e)}")



delete_duplicates_cross_files(
    filepath_1='../../data/clean/train_clean.csv',
    filepath_2='../../data/clean/test_clean.csv'
)
