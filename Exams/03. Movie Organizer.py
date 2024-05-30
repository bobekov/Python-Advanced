def movie_organizer(*args):
    movies = {}
    for movie, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)

    result = []
    sorted_movies = dict(sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in sorted_movies.items():
        sort_value = sorted(value)
        result.append(f"{key} - {len(value)}")
        for film in sort_value:
            result.append(f"* {film}")

    return '\n'.join(result)
