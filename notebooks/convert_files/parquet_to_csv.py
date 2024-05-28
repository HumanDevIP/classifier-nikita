from fastparquet import ParquetFile
import pandas as pd



def convert_parquet_to_csv(parquet_path: str, csv_path: str) -> None:
    try:
        pf: ParquetFile = ParquetFile(parquet_path)
        data_frame: pd.DataFrame = pf.to_pandas()
        data_frame.to_csv(csv_path, index=False)
        print(f"File converted successfully and saved to {csv_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")



convert_parquet_to_csv(parquet_path='../../data/train.parquet', csv_path='../../data/train.csv')
