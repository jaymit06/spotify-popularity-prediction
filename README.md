# Spotify Popularity Prediction Using Audio Features

## Overview

This project explores the relationship between Spotify audio features and song popularity using Exploratory Data Analysis (EDA) and Machine Learning.

The objective was to determine whether a song's audio characteristics alone can be used to predict its popularity score and identify which features contribute most to popularity.

The project includes:

- Data Exploration and Visualization
- Correlation Analysis
- Hit vs Flop Comparison
- Linear Regression
- Feature Scaling with StandardScaler
- Random Forest Regression
- Streamlit Deployment

---

## Dataset

Dataset: Spotify Tracks Dataset

The dataset contains over **586,000 songs** with audio features such as:

- Danceability
- Energy
- Loudness
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Tempo
- Duration

Target Variable:

- Popularity (0-100)

The dataset used for this project is not included in the repository due to GitHub file size limitations. Place tracks.csv inside the data/ folder before running the notebook.
---

## Project Workflow

### 1. Data Exploration

Initial exploration was performed to understand:

- Dataset dimensions
- Data types
- Feature distributions
- Missing values

---

### 2. Exploratory Data Analysis

Several visualizations were created to investigate relationships between audio features and popularity.

Key analyses included:

- Popularity Distribution
- Correlation Heatmap
- Popularity vs Loudness
- Popularity vs Energy
- Popularity vs Danceability
- Popularity vs Acousticness
- Popularity vs Instrumentalness

---

### 3. Hit vs Flop Analysis

Songs were divided into:

- Hits (Popularity ≥ 70)
- Flops (Popularity ≤ 20)

Feature averages were compared to identify characteristics associated with successful songs.

### Key Findings

- Popular songs tend to be louder.
- Popular songs tend to have higher energy.
- Popular songs are generally more danceable.
- Acoustic songs are less likely to be highly popular.
- Instrumental tracks are less likely to become mainstream hits.
- Song duration showed little relationship with popularity.

---

### 4. Machine Learning Models

Three approaches were evaluated:

| Model | MAE | R² |
|---------|---------|---------|
| Linear Regression | 13.31 | 0.195 |
| Linear Regression + Scaling | 13.18 | 0.209 |
| Random Forest Regression | 11.31 | 0.380 |

### Best Model

Random Forest Regressor

Performance:

- MAE: 11.31
- R²: 0.38

---

## Feature Importance

According to the Random Forest model, the most influential features were:

1. Acousticness
2. Loudness
3. Duration
4. Valence
5. Danceability

---

## Conclusion

Audio features provide useful information about song popularity, but they cannot fully explain a song's success.

The best-performing model achieved an R² score of approximately 0.38, suggesting that many important factors are not captured by audio characteristics alone.

Examples of missing factors include:

- Artist popularity
- Marketing and promotion
- Playlist placement
- Social media trends
- Cultural relevance
- Timing of release

This demonstrates that popularity is influenced by both the music itself and external factors.

---

## Streamlit Application

A Streamlit application was built to allow users to:

- Input Spotify audio features
- Predict song popularity using the trained Random Forest model

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

## Future Improvements

Potential improvements include:

- Incorporating artist-level features
- Adding playlist and streaming data
- Building a virality prediction model
- Using XGBoost or Gradient Boosting models
- Collecting social media engagement metrics

---

## Author

Jaymit Shriyan

B.Tech Data Science Student

Interested in Data Science, Machine Learning, Music Analytics, and Predictive Modeling.
