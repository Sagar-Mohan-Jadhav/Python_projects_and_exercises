# create an application where you can add/remove a movie from your movie collection, add info about the movie,
# change info about the movie, and also you can get information about the movie in your collection.

def add_movie():
    movie_name = input("Enter the name of the movie you want to add: ")
    if movie_name.title() in movies:
        print("This movie is already present in your movie collection.\n")
    else:
        movies.append(movie_name.title())
        add_movie_info(movie_name.title())


def add_movie_info(movie_name):
    print(f"What is the genre of {movie_name}? ")
    movie_genre = input()
    print(f"Who is the director of {movie_name}? ")
    movie_director = input()
    director_genre = f"{movie_name} is a {movie_genre.title()} movie and it is directed by {movie_director.title()}.\n"
    movie_info[movie_name] = director_genre


def remove_movie():
    movie_name = input("Enter the name of the movie you want to remove: ")
    if movie_name.title() in movies:
        movies.remove(movie_name.title())
        del movie_info[movie_name.title()]
    else:
        print(f"{movie_name.title()} is already not there in your movie collection\n")


def get_info():
    movie_name = input('Enter the name of the movie you want to know more about: ')
    if movie_name.title() in movies:
        print(f"Name: {movie_name.title()}\n"
              f"Info: {movie_info[movie_name.title()]}\n\n")
    else:
        print(f"{movie_name.title()} doe not exist in your movie collection, you may want to add it first.\n")


def change_info():
    movie_name = input("Enter the name of the movie you want to change the info about: ")
    if movie_name.title() in movies:
        add_movie_info(movie_name.title())
    else:
        print("This movie does not exist in your collection, you may want to add it first.\n")


prog_on = True
movies = []
movie_info = {}
while prog_on:
    print("Enter 1, if you want to add a movie to your collection.\n"
          "Enter 2, if you want to remove a movie from your collection.\n"
          "Enter 3, if you want to know more about a certain movie in your collection.\n"
          "Enter 4, if you want the entire list of of your movie collection.\n"
          "Enter 5, to change the info about a certain movie.\n"
          "Enter q, to exit the program.")
    user_choice = input()
    if user_choice == 'q':
        print("Have a nice day, bye bye.")
        prog_on = False
    elif user_choice == '1':
        add_movie()
    elif user_choice == '2':
        remove_movie()
    elif user_choice == '3':
        get_info()
    elif user_choice == '4':
        print(movie for movie in movies)
    elif user_choice == '5':
        change_info()
