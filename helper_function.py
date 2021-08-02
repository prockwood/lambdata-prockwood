import pandas as pd

def null_count(df):
    return df.isna().sum().sum()

def train_test_split(df, frac):
    choice_len = round(len(df) * frac)
    train_index = np.random.choice(len(df), choice_len, replace=False) 
    test_index = list(set(np.arange(len(df))) - set(train_index))

    return (df.iloc[train_index], df.iloc[test_index])
