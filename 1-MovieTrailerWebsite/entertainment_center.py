import Movie
import fresh_tomatoes

import simplejson

MOVIES_FILE = "movies.json"

def main():
    with open(MOVIES_FILE) as data_file:

        # Load JSON data as standard (non unicode) strings.
        movie_data = simplejson.loads(data_file.read())

        # Inflate live Movies from the dicts created from the JSON.
        # Note use of dict unpacking.
        movies = [Movie.Movie(**movie) for movie in movie_data]
        fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
