import json
import urllib.request

from Movie import Movie

class MovieListBuilder:
    movie_list = []

    # Retrieves information from the API and returns a JSON file
    def retrieve_api_info(self):
        response = urllib.request.urlopen(self.url)
        return response.read()

    # Converts JSON information into string format
    def json_information(self):
        convert_to_string = json.loads(self.retrieve_api_info())
        return convert_to_string

    # Parses information to return Movie object containing the Title,
    # release date, movie rating, and the movie's internal database
    # ID
    def get_result_at_index(self, data, index):
        result_at_index = data[index]
        title = result_at_index['original_title']
        release_date = self.get_year(result_at_index['release_date'])
        rating = result_at_index['vote_average']
        movie_id = result_at_index['id']
        movie = Movie(title, release_date, rating, movie_id)
        return movie

    # Returns a string contianing the year the movie was released
    def get_year(self, full_date):
        return full_date[0:4]

    # Generates a list of movies from user query
    def generate_movie_list(self):
        raw_data = self.json_information()
        all_results = raw_data['results']
        for item in all_results:
            movie_info = self.get_result_at_index(all_results, all_results.index(item))
            self.movie_list.append(movie_info)

    # Returns list of Movies
    def get_movie_list(self):
        return self.movie_list

    def __init__(self, url):
        self.url = url

api_url = "https://api.themoviedb.org/3/search/movie?api_key=ddc5407839c0e22afe0624dd5f3f4235&language=en-US&query=Avatar&page=1&include_adult=false"
test1 = MovieListBuilder(api_url)
test1.generate_movie_list()
#raw_set = test1.parse_information()
#reponse = test1.retrieve_api_info()
movies = test1.get_movie_list()
print(movies)
#print(reponse)
