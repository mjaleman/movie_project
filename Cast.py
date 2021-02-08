from Movie import Movie

class Cast(Movie):
    def __init__(self, title, released, rating, movie_id, actor1, actor2, actor3, director):
        super().__init__(title, release_year, rating, movie_id)
        self.actor1 = actor1
        self.actor2 = actor2
        self.actor3 = actor3
        self.director = director

    def get_actor1(self):
        return self.actor1

    def get_actor2(self):
        return self.actor2

    def get_actor3(self):
        return self.actor3

    def get_director(self):
        return self.director


