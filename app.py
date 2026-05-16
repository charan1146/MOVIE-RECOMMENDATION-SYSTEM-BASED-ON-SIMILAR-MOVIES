import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

# Title
st.title("🎬 AI Movie Recommendation System")

# Description
st.write("Get movie recommendations based on genre.")

# Read CSV file
movies = pd.read_csv("movies.csv")

# User input
movie_name = st.text_input("Enter movie name:")

# Recommendation logic
if movie_name:

    # Convert input to lowercase
    movie_name_lower = movie_name.lower()

    # Find movie in dataset
    selected_movie = movies[
        movies['movie'].str.lower() == movie_name_lower
    ]

    # If movie exists
    if not selected_movie.empty:

        # Get genre
        genre = selected_movie.iloc[0]['genre']

        # Find similar movies
        recommendations = movies[
            movies['genre'] == genre
        ]

        st.success(f"Recommended {genre} movies:")

        # Display recommendations
        for movie in recommendations['movie']:
            if movie.lower() != movie_name_lower:
                st.write("👉", movie)

    # If movie not found
    else:
        st.error("Movie not found in database.")

# Footer
st.write("---")
st.caption("Developed using Python, Pandas, and Streamlit")