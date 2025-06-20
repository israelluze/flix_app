import streamlit as st 
from actors.repository import ActorsRepository

class ActorsService:

    def __init__(self):
        self.actors_repository = ActorsRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actors_repository.get_actors()
        st.session_state.actors = actors        
        return actors
    
    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        new_actor = self.actors_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor