import os 
import sys
import pandas as pd
from typing import List, Dict 

def merge_files(df1:pd.DataFrame, df2:pd.DataFrame)->pd.DataFrame:
    """
    Function to merge and shuffle two Pandas DataFrames
    """
    return pd.concat([df1, df2]).sample(frac=1)

def perform_mask(df, dup_column, drug_word_col, treatment_word_col, replace_labels):
    """
    Masks certain words to follow GAD training format.
    """
    df[dup_column] = df.map(lambda x: x[dup_column].replace(drug_word_col, replace_labels[0]))
    df[dup_column] = df.map(lambda x: x[dup_column].replace(treatment_word_col, replace_labels[1]))
    return df 

def read_convert_annotated_data(file_path:str, output_path:str, out_columns:List[str]=["sentence", "target"], 
                                    dup_column='sentence', mask=False)->None:
    """
    Converts our annotated data file
    """
    df = pd.read_excel(file_path).drop_duplicates(subset='dup_column')
    df['target'] = df['Target']
    if mask:
        df = perform_mask(df, dup_column, 'drug', 'treatment', ["@DISEASE$", "@GENE$"])
    df[out_columns].to_csv(output_path, header=False, index=False, sep='\t')

def format_df(postives_path:str, negatives_path:str, output_path:str, dup_column='sentence',
                out_columns:List[str]=["sentence", "target"], mask=False, rename_map:Dict={})->None:
    """
    Formats positive and negative df to work
    """
    positive_df = pd.read_csv(postives_path)
    negative_df = pd.read_csv(negatives_path).rename(columns={'new_sentence': 'sentence', "word_drug":'drug', 'inserted_word':"treatment"})
    combined_df = merge_files(positive_df, negative_df)
    if mask:
        combined_df = perform_mask(combined_df, dup_column, 'drug', 'treatment', ["@DISEASE$", "@GENE$"])
    combined_df[out_columns].to_csv(output_path, header=False, index=False, sep='\t')

