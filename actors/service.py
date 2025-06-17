from actors.repository import ActorsRepository

class ActorsService:

    def __init__(self):
        self.actors_repository = ActorsRepository()

    def get_actors(self):
        return self.actors_repository.get_actors()
    
    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        return self.actors_repository.create_actor(actor)    