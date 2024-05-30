import pandas as pd
from transformers import BertTokenizer



def check_and_remove_token_overruns(max_token_limit, origin_path, output_path):
    df = pd.read_csv(origin_path)
    
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # Function to calculate the total number of tokens
    def calculate_tokens(row):
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
