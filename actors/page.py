import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorsService


def show_actors():
    actors_service = ActorsService()
    actors = actors_service.get_actors()
        
    actors_df = pd.json_normalize(actors)

    if not actors_df.empty:

        st.write('Lista de Atores/Atrizes')

        AgGrid(
            data=pd.DataFrame(actors_df),        
            key='actors_grid'
            )
    else:
        st.warning('Nenhum Ator/Atriz encontrado!')
    
    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1600,1,1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    ),
    nationality_dropdown = ['Brazil', 'American','Others']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown
    )
    if st.button('Cadastrar'):
        new_actor = actors_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastra o(a) Ator/Atriz. Verifique os campos')        