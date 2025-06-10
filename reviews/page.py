import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {        
        "id": 1,
        "stars": 5,
    },
    {        
        "id": 2,
        "stars": 3,  
    },
    {        
        "id": 3,
        "stars": 2,
    }
]

def show_reviews():
    st.write('Lista de Reviews')
    
    AgGrid(
        data=pd.DataFrame(movies),        
        key='reviews_grid'
        )
    
    st.title('Cadastrar novo Reviews')
    name = st.text_input('review do Filme')
    if st.button('Cadastrar'):
        st.success(f'Filme {name} cadastrado com sucesso!')
    