import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorsService


def show_actors():
    actors_service = ActorsService()
    actors = actors_service.get_actors()
    print(actors)
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
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz {name} cadastrado(a) com sucesso!')    