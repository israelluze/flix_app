from movies.repository import MoviesRepository

class MoviesService:

    def __init__(self):
        self.movies_repository = MoviesRepository()

    def get_movies(self):
        return self.movies_repository.get_movies()
    
    def create_movie(self, title, release_date, genre, actors, resume):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume
        )
        return self.movies_repository.create_movie(movie)    
    
    def get_movie_stats(self):
        return self.movies_repository.get_movie_stats()