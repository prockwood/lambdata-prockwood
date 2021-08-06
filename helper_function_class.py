import pandas as pd
import numpy as np

# A collection of helpful DataFrame functions
class Helper:

    def __init__(self, df):
        self.df = df

    # Count all NaN/Nulls in a DataFrame.
    def null_count(self):
        return self.df.isna().sum().sum()


    # Splts a DataFrame into two,
    # frac is the size of the first piece
    # as a proportion of the DataFrame size.
    def train_test_split(self, frac):
        choice_len = round(len(self.df) * frac)
        train_index = np.random.choice(len(self.df), choice_len, replace=False)
        test_index = list(set(np.arange(len(self.df))) - set(train_index))
        return (self.df.iloc[train_index], self.df.iloc[test_index])


    # shuffles all datum in a DataFrame on both axis.
    def randomize(self, seed):
        np.random.seed(seed)
        flat_df = self.df.to_numpy().flatten()
        np.random.shuffle(flat_df)
        re_rect = flat_df.reshape(self.df.shape)
        return pd.DataFrame(data=re_rect, columns=self.df.columns)

