import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MoviesService




def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()
    
    if reviews:
        
        st.write('Lista de Reviews')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=pd.DataFrame(reviews_df),        
            key='reviews_grid'
            )
    else:
        st.warning('Nenhuma avaliação encontrada')    
    
    st.title('Cadastrar novo Reviews')
    
    movie_service = MoviesService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))
    
    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1        
    )
    comment = st.text_area('Comentário')
    
    if st.button('Cadastrar'):        
        review_create = review_service.create_review(
            comment=comment,
            movie=movie_titles[selected_movie_title],
            stars=stars
        )
        if review_create:
            st.rerun()
        else:
            st.error('Erro ao criar review. Verifique as informações')
    