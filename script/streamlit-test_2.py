import streamlit as st
import pickle
import pandas as pd
import re
import difflib
from recommender_module import item_based_recommender

movie_ratings = pd.read_csv('F:\coding\Bootcamp\Section8\data\dense_matrix.csv')

st.title("Movie Recommender")
 
st.write("""
### Project description
We have trained a model to help you find something to watch on Friday.""")

title = str(st.text_input("Gimme a movie:"))
closest_match = difflib.get_close_matches(title, movie_ratings['title'], n=1).pop(0)

st.write(f'Showing recommendations for: {closest_match}', 
            item_based_recommender(dense_matrix=movie_ratings, 
            title=closest_match, n=5))
