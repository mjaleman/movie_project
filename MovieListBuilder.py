import json
import urllib.request

from Movie import Movie

class MovieListBuilder:
    movie_list = []

    def retrieve_api_info(self):
        response = urllib.request.urlopen(self.url)
        return response.read()

    def json_information(self):
        convert_to_string = json.loads(self.retrieve_api_info())
        return convert_to_string

    def get_result_at_index(self, data, index):
        result_at_index = data[index]
        title = result_at_index['original_title']
        release_date = self.get_year(result_at_index['release_date'])
        rating = result_at_index['vote_average']
        movie = Movie(title, release_date, rating)
        return movie

    def get_year(self, full_date):
        return full_date[0:4]

    def generate_movie_list(self):
        raw_data = self.json_information()
        all_results = raw_data['results']
        for item in all_results:
            movie_info = self.get_result_at_index(all_results, all_results.index(item))
            self.movie_list.append(movie_info)

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
