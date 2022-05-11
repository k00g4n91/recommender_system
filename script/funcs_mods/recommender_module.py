import pandas as pd


def get_user_prefered_item(dense_matrix: pd.DataFrame, user: int):
    
    data = dense_matrix.copy()

    return(
    data
        .query('userId == @user')
        .sort_values('rating', ascending=False)
        .reset_index()
        ['title'][0]
        )



def item_based_recommender(dense_matrix: pd.DataFrame, title:str, n=5):

    def get_sparse_matrix(dense_matrix: pd.DataFrame):
        return(
        dense_matrix
            .pivot_table(values='rating',columns='title', index='userId')
            .fillna(0))


    sparse_matrix = get_sparse_matrix(dense_matrix)
    
    return(
    sparse_matrix
        .corrwith(sparse_matrix[title])
        .sort_values(ascending=False)
        .index
        .to_list()[1:n+1])
    

