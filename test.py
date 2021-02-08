from Movie import Movie
from CastBuilder import CastBuilder

new_movie = Movie("Avatar", "2009", "7.5", 19995)
print(new_movie)
cast_instance = CastBuilder(new_movie)
print(cast_instance.get_cast_link())
