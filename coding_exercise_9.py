class Movie:
    def __init__(self, name, director):
        self.movie_name = name
        self.movie_director = director

    def print_info(self):
        return print(f'<<{self.movie_name}>> by {self.movie_director}')


my_movie = Movie('The Matrix', 'Wachowski')
my_movie.print_info()
