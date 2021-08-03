import pandas as pd
import numpy as np

def null_count(df):
    return df.isna().sum().sum()

def train_test_split(df, frac):
    choice_len = round(len(df) * frac)
    train_index = np.random.choice(len(df), choice_len, replace=False)
    test_index = list(set(np.arange(len(df))) - set(train_index))
    return (df.iloc[train_index], df.iloc[test_index])

def randomize(df, seed):
    np.random.seed(seed)
    flat_df = df.to_numpy().flatten()
    np.random.shuffle(flat_df)
    re_rect = flat_df.reshape(df.shape)
    return pd.DataFrame(data=re_rect, columns=df.columns)
