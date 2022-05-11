import streamlit as st
import pickle
import pandas as pd
import re
import difflib
from recommender_module import item_based_recommender

movie_ratings = pd.read_csv('F:\coding\Bootcamp\Section8\data\dense_matrix.csv')

st.title("Movie Recommender")
 
st.write("""
### Easing the agony of choice""")



st.write("""##### Most Popular""")
def popularity_recommender():
    df = (movie_ratings
        .groupby(['title'])
        .agg(popularity = ('rating','count'),
            quality = ('rating', 'mean'))
        .query('popularity >= 200')
        .sort_values('quality', ascending=False)
    ).reset_index()
    return df.iloc[:5,:1]

st.write(popularity_recommender())

st.write("""##### Recommendations""")

user_movie = str(st.text_input("Gimme a movie:"))

closest_match = difflib.get_close_matches(user_movie, movie_ratings['title'], n=1,cutoff=0.5).pop(0)

st.write(f'Showing recommendations for: {closest_match}', 
            item_based_recommender(dense_matrix=movie_ratings, 
            title=closest_match, n=5))







