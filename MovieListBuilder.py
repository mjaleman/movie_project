import json
import urllib.request

class MovieListBuilder:
    movie_list = []

    def retrieve_api_info(self):
        response = urllib.request.urlopen(self.url)
        return response.read()

    def json_information(self):
        convert_to_string = json.dumps(self.retrieve_api_info())
        convert_to_jobject = json.loads(convert_to_string)
        return convert_to_string

    def parse_information(self):
        raw_data = self.json_information()
        all_results = raw_data['results']
        return all_results

    def __init__(self, url):
        self.url = url

api_url = "https://api.themoviedb.org/3/search/movie?api_key=ddc5407839c0e22afe0624dd5f3f4235&language=en-US&query=Avatar&page=1&include_adult=false"
test1 = MovieListBuilder(api_url)
#raw_set = test1.parse_information()
reponse = test1.retrieve_api_info()
print(reponse)
