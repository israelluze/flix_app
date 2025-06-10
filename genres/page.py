import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


genres = [
    {
        "id": 2,
        "name": "Comédia"
    },
    {
        "id": 4,
        "name": "Romance"
    },
    {
        "id": 5,
        "name": "Dramas"
    },
    {
        "id": 6,
        "name": "Suspense"
    },
    {
        "id": 7,
        "name": "Ação"
    },
    {
        "id": 9,
        "name": "Ficção Científica"
    }
]

def show_genres():
    st.write('Lista de Gêneros')
    
    AgGrid(
        data=pd.DataFrame(genres),        
        key='genres_grid'
        )
    
    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero {name} cadastrado com sucesso!')
    