
import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API setup
st.set_page_config(page_title="Spotify Recommender", page_icon="🎵", layout="centered")
client_id = "56b7c56af24e417da49d5739ee50ca47"
client_secret = "e40453a57417459bb88c1f9756c31e3d"

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = Spotify(auth_manager=auth_manager)

df = pd.read_csv("SpotifyFeatures.csv") 

from sklearn.preprocessing import StandardScaler

features = ['danceability', 'energy', 'valence', 'tempo', 'acousticness']
X_scaled = StandardScaler().fit_transform(df[features])


def get_album_cover(track_name, artist_name):
    query = f"{track_name} {artist_name}"
    result = sp.search(q=query, type='track', limit=1)
    try:
        return result['tracks']['items'][0]['album']['images'][0]['url']
    except (IndexError, KeyError):
        return None



def recommend(song_name, df, features_scaled, top_n=10):
    index = df[df['track_name'] == song_name].index[0]
    similarity = cosine_similarity([features_scaled[index]], features_scaled)[0]
    similar_indices = similarity.argsort()[::-1][1:top_n+1]
    results = df.iloc[similar_indices][['track_name', 'artist_name']].copy()
    results['album_cover'] = results.apply(
        lambda row: get_album_cover(row['track_name'], row['artist_name']), axis=1
    )
    return results


st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
    }

    .stApp {
        background-color: transparent;
    }

    .block-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background-color: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 12px;
        color: white;
    }

    @media only screen and (max-width: 600px) {
        .block-container {
            padding: 1rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #1DB954;'>Spotify Music Recommendation System</h1>", unsafe_allow_html=True)

song_list = df['track_name'].dropna().unique()
selected_song = st.selectbox("Choose a song:", song_list)


col1, col2 = st.columns([1, 1])
with col1:
    recommend_button = st.button("Recommend Similar Songs")
with col2:
    reset_button = st.button("Reset")

if recommend_button:
    with st.spinner("Fetching recommendations..."):
        recommendations = recommend(selected_song, df, X_scaled)

    for i, row in recommendations.iterrows():
        st.markdown(f"### {row['track_name']} by {row['artist_name']}")
        if row['album_cover']:
            st.image(row['album_cover'], width=200)
        else:
            st.write("No album cover found.")

elif reset_button:
    st.experimental_rerun()

st.markdown(
    "<hr style='margin-top: 3rem; margin-bottom: 1rem;'>"
    "<p style='text-align: center; font-size: 14px;'>Made by Ziggy Greg | "
    "<a href='https://github.com/ziggy-greg' target='_blank'>GitHub</a> | "
    "<a href='https://instagram.com/your_handle' target='_blank'>Instagram</a></p>",
    unsafe_allow_html=True
)