import streamlit as st
from recommender import recommend, model_movies
import urllib.parse

st.markdown("""
<style>
/* Full app background */
.stApp {
    background-color: #0f172a;
    color: #e5e7eb;
}

/* Title */
h1, h2, h3 {
    color: #f9fafb;
}

/* Dropdown & buttons */
div[data-baseweb="select"] > div {
    background-color: #111827;
    color: white;
}

button {
    background-color: #e50914 !important;
    color: white !important;
    border-radius: 8px;
    font-weight: 600;
}

/* Links */
a {
    color: #60a5fa !important;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.markdown("""
<h1 style='font-size:42px;'>🎬 Movie Recommendation System</h1>
<p style='color:#9ca3af;font-size:16px;'>
Discover movies you’ll love, based on what you already enjoy
</p>
""", unsafe_allow_html=True)


movie_name = st.selectbox(
    "Choose a movie",
    model_movies.sort_values().values
)

movie_id = model_movies[model_movies == movie_name].index[0]

if st.button("Recommend"):
    st.subheader("Recommended Movies:")

from recommender import recommend, model_movies, get_movie_poster
import urllib.parse
import streamlit as st

if st.button("Recommend", key="recommend_btn"):

    st.markdown("<h2>Recommended Movies</h2>", unsafe_allow_html=True)

    recommended_movies = recommend(movie_id)
    recommended_movies = recommended_movies[:5]  # limit to 5 (clean UI)

    cols = st.columns(len(recommended_movies))

    for col, movie in zip(cols, recommended_movies):
        poster = get_movie_poster(movie)
        query = urllib.parse.quote(movie)
        imdb_url = f"https://www.imdb.com/find?q={query}"

        with col:
            st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

            if poster:
                st.image(poster, width=170)
            else:
                st.markdown(
                    "<div style='height:250px;background:#1f2937;"
                    "display:flex;align-items:center;justify-content:center;"
                    "border-radius:8px;color:#9ca3af;'>No Poster</div>",
                    unsafe_allow_html=True
                )

            st.markdown(
                f"<p style='margin-top:10px;font-size:14px;'>"
                f"<a href='{imdb_url}' target='_blank'>{movie}</a></p>",
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)
