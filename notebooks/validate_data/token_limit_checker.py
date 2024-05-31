import pandas as pd
from pandas import DataFrame
from transformers import BertTokenizer



def check_and_remove_token_overruns(max_token_limit, origin_path, output_path):
    """
    Identify and remove rows with token overruns in a CSV file.

    This function reads a CSV file, calculates the total number of tokens in specified text columns using the BERT tokenizer,
    removes rows that exceed the maximum token limit, and saves the cleaned data back to a CSV file.

    Arguments:
    - max_token_limit (int): The maximum number of tokens allowed per row.
    - origin_path (str): The path to the input CSV file.
    - output_path (str): The path where the cleaned CSV file will be saved.

    Return Value:
    - tuple: A tuple containing the number of rows with token overruns and the number of deleted rows.
    """
    
    df: DataFrame = pd.read_csv(origin_path)
    
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # Function to calculate the total number of tokens
    def calculate_tokens(row) -> int:
        tokens_text = tokenizer.tokenize(row['text'])
        tokens_text_b = tokenizer.tokenize(row['text_b'])
        
        total_tokens = tokens_text + ['[SEP]'] + tokens_text_b
        
        return len(total_tokens)
    
    df['token_count'] = df.apply(calculate_tokens, axis=1)
    
    overruns = df[df['token_count'] > max_token_limit]
    
    df_cleaned = df[df['token_count'] <= max_token_limit]
    
    df_cleaned = df_cleaned.drop(columns=['token_count'])
    
    df_cleaned.to_csv(output_path, index=False)
    
    num_overrun_rows = len(overruns)
    num_deleted_rows = len(df) - len(df_cleaned)
    
    return num_overrun_rows, num_deleted_rows



max_token_limit = 512
origin_path = '../../data/clean/train_clean.csv'
output_path = '../../data/clean/train_clean.csv'
num_overrun_rows, num_deleted_rows = check_and_remove_token_overruns(max_token_limit, origin_path, output_path)
print(f"Number of rows with token overruns: {num_overrun_rows}")
print(f"Number of deleted rows: {num_deleted_rows}")
