from actors.repository import ActorsRepository

class ActorsService:

    def __init__(self):
        self.actors_repository = ActorsRepository()

    def get_actors(self):
        return self.actors_repository.get_actors()