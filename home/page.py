import streamlit as st 
import plotly.express as px
from movies.service import MoviesService


def show_home():
    movie_service = MoviesService()
    movie_stats = movie_service.get_movie_stats()
    
    st.title('Estatísticas de filmes')
    
    if len(movie_stats['movies_by_genre']) > 0 :
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero'
        )
        st.plotly_chart(fig)
    
    st.subheader('Total de Filmes Cadastrados:')
    for genre in movie_stats['movies_by_genre']:
        st.write(f'{genre['genre__name']}: {genre['count']}')
    
    st.subheader('Total de Avaliações Cadastradas:')
    st.write(movie_stats['total_reviews'])
    
    st.subheader('Total Geral de Estrelas nas Avaliações:')
    st.write(movie_stats['average_stars'])