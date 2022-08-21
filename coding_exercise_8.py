'''
As part of this exercise you won't have to print anything or get any user input.

Here's a representation of a movie as a dictionary:

{
  'name': 'The Matrix',
  'director': 'Wachowski'
}
How would you write this as a class, so that an object can be created like this?

my_movie = Movie('The Matrix', 'Wachowski')
Happy coding!

— Jose and the Teclado team

P.S. Remember you'll need to define an __init__  method, which needs to have two underscores at each side.
'''


class Movie:
    def __init__(self, name, director):
        self.movie_name = name
        self.movie_director = director


mov = {
    'name': 'The Matrix',
    'director': 'Wachowski'
}

my_movie = Movie('The Matrix', 'Wachowski')


