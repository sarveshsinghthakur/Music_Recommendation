import streamlit as st
import pandas as pd
import pickle

music_data = pickle.load(open("song_list.pkl", "rb"))

def recommend(song_title):
    song_title = song_title.lower()
    matched_songs = music_data[music_data['ï»¿Song-Name'].str.lower().str.contains(song_title)]
    
    if matched_songs.empty:
        return f"Music '{song_title}' not found in the dataset."
    
    first_song_artists = matched_songs.iloc[0]['Singer/Artists']
    recommendations = music_data[music_data['Singer/Artists'].apply(lambda artists: any(artist in first_song_artists for artist in artists))].head(5)
    
    return recommendations[['ï»¿Song-Name', 'Singer/Artists']].values.tolist()

st.title("Music Recommendation System")
user_input = st.text_input("Enter a music title:")

if user_input:
    recommendations = recommend(user_input)
    if isinstance(recommendations, str):
        st.write(recommendations)
    else:
        st.write(f"Songs similar to '{user_input}':")
        for idx, rec in enumerate(recommendations, 1):
            st.write(f"**{idx}. Song**: {rec[0]}  \n**Artists**: {', '.join(rec[1])}")
