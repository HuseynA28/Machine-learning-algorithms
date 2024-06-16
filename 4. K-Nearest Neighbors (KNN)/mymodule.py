import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def check_df(dataframe, head=3):

    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Duplicate Values #####################")
    print(dataframe.duplicated().sum())
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Unique Values #####################")
    print(dataframe.nunique())

def find_categorical_columns(df, max_unique_values=7):
    categorical_cols = []
    for col in df.columns:
        dtype = str(df[col].dtypes)
        num_unique_values = df[col].nunique(dropna=False)

        # Check if the column is a categorical type or has a limited number of unique values
        if dtype in ["category", "object", "bool"] or (num_unique_values <= max_unique_values):
            categorical_cols.append(col)

    return categorical_cols



def binary_columns_find(df):
    binary_cols = []
    for col in df.columns:
      
        unique_values = df[col].dropna().unique()
 
        num_unique_non_null = len(unique_values)
        
        has_nan = df[col].isnull().any()

        if (num_unique_non_null == 1 and has_nan) or num_unique_non_null == 2:
            binary_cols.append(col)

    return binary_cols




    