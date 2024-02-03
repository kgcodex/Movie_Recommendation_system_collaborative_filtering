#importing Modules
import streamlit as st 
import pandas as pd 
import pickle
import time

# Title
st.title("Movie Recommender System")

# Loading DataFrame
movies=pd.read_csv("movies.csv")

similarity=pickle.load(open("similarity.pkl","rb"))
similarity=pd.DataFrame(similarity)

# Fetching Movies
def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    movie_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x: x[1])[1:6]

    for i in movie_list:
        st.write(movies.iloc[i[0]].title)
        time.sleep(0.5)
        

# Search Box
selected_movie=st.selectbox(
"Select your Movie",
movies["title"].values)

# Recommend Button
if st.button("Recommend"):
    recommend(selected_movie)