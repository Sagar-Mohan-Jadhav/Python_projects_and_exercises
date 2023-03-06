class Movie:
    def __init__(self, name, director):
        self.movie_name = name
        self.movie_director = director

    def print_info(self):
        return print(f'<<{self.movie_name}>> by {self.movie_director}')


mov = {'name': 'The Matrix', 'director': 'Wachowski'}
my_movie = Movie(mov['name'], mov['director'])
my_movie.print_info()
