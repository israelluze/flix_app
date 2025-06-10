import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

actors = [
    {
        "id": 1,
        "name": "Silvester Stalone",
        "date_of_birth": "1980-01-01",
        "nationality": "Other"
    },
    {
        "id": 2,
        "name": "Leonardo d'Caprio",
        "date_of_birth": "1974-11-11",
        "nationality": "American"
    },
    {
        "id": 3,
        "name": "Kate Winslet",
        "date_of_birth": "1990-01-01",
        "nationality": "Canadian"
    },
    {
        "id": 4,
        "name": "Kathy Bates",
        "date_of_birth": "1970-01-01",
        "nationality": "Other"
    },
    {
        "id": 5,
        "name": "Julia Roberts",
        "date_of_birth": "1967-10-28",
        "nationality": "American"
    },
    {
        "id": 6,
        "name": "Wagner Moura",
        "date_of_birth": "1976-06-27",
        "nationality": "Brazilian"
    },
    {
        "id": 7,
        "name": "Camila Mendes",
        "date_of_birth": "1994-06-29",
        "nationality": "Brazilian"
    }
]

def show_actors():
    st.write('Lista de Atores/Atrizes')

    AgGrid(
        data=pd.DataFrame(actors),        
        key='actors_grid'
        )
    
    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz {name} cadastrado(a) com sucesso!')    