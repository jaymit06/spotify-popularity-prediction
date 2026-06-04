import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    return joblib.load("spotify_popularity_model.pkl")

model = load_model()

st.title("Spotify Popularity Predictor")
st.write(
    "Enter song features below and predict Spotify popularity."
)

danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
energy = st.slider("Energy", 0.0, 1.0, 0.5)
loudness = st.slider("Loudness", -60.0, 5.0, -10.0)
speechiness = st.slider("Speechiness", 0.0, 1.0, 0.1)
acousticness = st.slider("Acousticness", 0.0, 1.0, 0.5)
instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.0)
liveness = st.slider("Liveness", 0.0, 1.0, 0.1)
valence = st.slider("Valence", 0.0, 1.0, 0.5)
tempo = st.slider("Tempo", 50.0, 250.0, 120.0)
duration_ms = st.slider("Duration (ms)", 30000, 600000, 210000)

input_data = pd.DataFrame(
    [[
        danceability,
        energy,
        loudness,
        speechiness,
        acousticness,
        instrumentalness,
        liveness,
        valence,
        tempo,
        duration_ms
    ]],
    columns=[
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "duration_ms"
    ]
)

if st.button("Predict Popularity"):
    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Popularity Score: {prediction:.1f}"
    )
