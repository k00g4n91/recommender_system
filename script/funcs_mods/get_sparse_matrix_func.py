import pandas as pd

def get_sparse_matrix(dense_matrix: pd.DataFrame):
        return(
        dense_matrix
            .pivot_table(values='rating',columns='title', index='userId')
            .fillna(0))