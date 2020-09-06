movies =['Terminator', 'Bambi','Rocky']
new_movies = ['Hunt for the Wilderpeople','Titanic', 'Batman']
movies.extend(new_movies)
del movies[1]
movies.sort()
for movie in movies:
    print(movie)
