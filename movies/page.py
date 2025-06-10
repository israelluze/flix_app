import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {        
        "title": "Titanic",       
    },
    {        
        "title": "Transformers",       
    },
    {        
        "title": "Super Mario",       
    },
]

def show_movies():
    st.write('Lista de Filmes')
    
    AgGrid(
        data=pd.DataFrame(movies),        
        key='movies_grid'
        )
    
    st.title('Cadastrar novo Filme')
    name = st.text_input('Nome do Filme')
    if st.button('Cadastrar'):
        st.success(f'Filme {name} cadastrado com sucesso!')
    