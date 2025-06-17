from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MoviesService
from actors.service import ActorsService
from genres.service import GenreService

def show_movies():
    movie_service = MoviesService()
    movies = movie_service.get_movies()
    
    if movies:
        movies_df = pd.json_normalize(movies) 
        movies_df = movies_df.drop(columns=['actors','genre.id'])   
        st.write('Lista de Filmes')
    
        AgGrid(
            data=pd.DataFrame(movies_df),        
            key='movies_grid'
            )
    else:
        st.warning('Nenhum filme encontrado')
    
    st.title('Cadastrar novo Filme')
    
    title = st.text_input('Título')
    
    release_date = st.date_input(
        label='Data de Lançamento',
        value=datetime.today(),
        min_value=datetime(1600,1,1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))
    
    actors_serice = ActorsService()
    actors = actors_serice.get_actors()
    actors_names = {actor['name']: actor['id'] for actor in actors}
    selected_actor_names = st.multiselect('Atores/Atrizes', list(actors_names.keys()))
    selected_actors_ids = [actors_names[name] for name in selected_actor_names]
    
    resume = st.text_area('Resumo')
    
    
    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme. Verifique os campos')
    