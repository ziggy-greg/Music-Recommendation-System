

# Spotify Music Recommendation System

A content-based music recommendation system that suggests songs similar to a selected track based on audio features such as danceability, energy, valence, tempo, and acousticness.

![Demo Screenshot](https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4)

## Features

- Recommends 10 similar songs based on a selected track
- Retrieves album covers using the Spotify API
- Clean, mobile-responsive UI built with Streamlit
- Styled background and container for a modern look
- Reset button to reload app state

## How It Works

1. The app uses cosine similarity  to find songs with similar audio characteristics.
2. Audio features are normalized using **StandardScaler**.
3. Album covers are fetched in real time via **Spotipy** (Spotify Web API).
4. Songs are displayed with cover art and artist names.

## Tech Stack

- **Python**
- **Streamlit** (Web UI)
- **Pandas**, **Scikit-learn** (Feature scaling & similarity)
- **Spotipy** (Spotify Web API wrapper)

## Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/ziggy-greg/Music-Recommendation-System.git
   cd Music-Recommendation-System

	2.	Install dependencies:

pip install -r requirements.txt


	3.	Add your Spotify credentials:
	•	Create an app at Spotify Developer Dashboard
	•	Replace client_id and client_secret in app.py
	4.	Run locally:

streamlit run app.py




Author

Ziggy Greg
	•	GitHub: @ziggy-greg
	

License

This project is licensed under the MIT License.

