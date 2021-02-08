import json
import urllib.request

from Movie import Movie

class CastBuilder:
    def __init__(self, movie):
        self.movie = movie
        self.movie_id = movie.movie_id

    # Returns link to JSON file for movie's cast
    def get_cast_link(self):
        cast_link = f"https://api.themoviedb.org/3/movie/{self.movie_id}/credits?api_key=ddc5407839c0e22afe0624dd5f3f4235&language=en-US"
        return cast_link

    def get_JSON_file(self):
        json_file = urllib.request.urlopen(self.get_cast_link())
        return json_file.read()

    def convert_to_readable(self):
        string_format = json.load(self.get_JSON_file())
        return string_format

