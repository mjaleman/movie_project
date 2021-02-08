class Movie:
    def __init__(self, title, release_year, rating, movie_id):
        self.title = title
        self.release_year = release_year
        self.rating = rating
        self.movie_id = movie_id

    def __repr__(self):
        string_representation = f"\n{self.title} -- {self.release_year} -- {self.rating}"
        return string_representation
    
    def description(self):
        return f"{self.name} was released with a budget of ${self.budget} in {self.release_year}.It was directed by {self.director}"

    def get_title(self):
        return self.title

    def get_release_year(self):
        return self.release_year

    def get_rating(self):
        return self.rating

    def get_movie_id(self):
        return movie_id


