 #1
def high_score(movie):
    return movie['imdb'] > 5.5
    print(high_score(movies[0]))

#2
def get_high_score_movies(movie_list):
    return [movie for movie in movie_list if high_score(movie)]
    high_score_movies = get_high_score_movies(movies)
    print(high_score_movies)

#3
def filter_by_category(movie_list, category):
    return [movie for movie in movie_list if movie['category'] == category]
    romance_movies = filter_by_category(movies, 'Romance')
    print(romance_movies)

#4
def average_imdb_score(movie_list):
    if not movie_list:
        return 0
    total_score = sum(movie['imdb'] for movie in movie_list)
    return total_score / len(movie_list)
    avg_score = average_imdb_score(movies)
    print(f"Average IMDB score for all movies: {avg_score}")

#5
def average_imdb_score_by_category(movie_list, category):
    category_movies = filter_by_category(movie_list, category)
    return average_imdb_score(category_movies)
    avg_score_romance = average_imdb_score_by_category(movies, 'Romance')
    print(f"Average IMDB score for Romance movies: {avg_score_romance}")