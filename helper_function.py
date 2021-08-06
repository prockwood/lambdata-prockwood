import pandas as pd
import numpy as np
import re

def null_count(df):
    """
    Returns the number of null values in the input DataFrame
    """
    return df.isna().sum().sum()

def train_test_split(df, seed, frac):
    """
    Takes a DataFrame and returns two DataFrames of randomly selected
    rows. The second argument sets a seed for the random generator.
    The third argument assigns the size of the first returned Dataframe.
    """
    np.random.seed(seed)
    choice_len = round(len(df) * frac)
    train_index = np.random.choice(len(df), choice_len, replace=False)
    test_index = list(set(np.arange(len(df))) - set(train_index))
    return (df.iloc[train_index], df.iloc[test_index])

def randomize(df, seed):
    """
    Takes a DataFrame and returns a DataFrame of equivalent shape with
    all elements shuffled on both axis. The second argument sets a seed
    for the random generator
    """
    np.random.seed(seed)
    flat_df = df.to_numpy().flatten()
    np.random.shuffle(flat_df)
    re_rect = flat_df.reshape(df.shape)
    return pd.DataFrame(data=re_rect, columns=df.columns)

def addy_split(series):
    """
    Takes a pandas Series of street addresses in the format:
    '30 Rockefeller Plaza/\nNew York, NY 10112' and returns a Dataframe
    with town, state, and zipcode broken-out into columns.
    """
    town = series.apply(lambda x: re.findall(r"\n(.*?),", x)[0])
    state = series.apply(lambda x: re.findall(r"[A-Z]{2}", x)[0])
    zip_c = series.apply(lambda x: re.findall(r"\d{5}", x)[0])
    return pd.DataFrame({'town': town, 'state': state, 'zip': zip_c})

def check_elements_eq(df1, df2):
    """
    Takes two DataFrames or Series' of equal shape and returns a boolean
    indicating whether all elements of the two objects are equivalent.
    Supports the comparison of null types, which pd.DataFrame.equal() does'nt.
    """

    if type(df1) == pd.core.series.Series:
        df1 = df1.to_frame().T
    if type(df2) == pd.core.series.Series:
        df2 = df2.to_frame().T

    if df1.shape != df2.shape:
#         print(df1.shape, df2.shape)
        raise Exception("df1 and df2 are not of the same shape")

    for i in range(df1.shape[0]):
        for j in range(df1.shape[1]):
            if pd.isna(df1.iloc[i,j]) == True:
                if pd.isna(df2.iloc[i,j]):
                    continue
                else:
                    print(f"Elements at position ({i}, {j}) are not equivalent.")
                    return False
            else:
                if df1.iloc[i,j] == df2.iloc[i,j]:
                    continue
                else:
                    print(f"Elements at position ({i}, {j}) are not equivalent.")
                    return False
    return True