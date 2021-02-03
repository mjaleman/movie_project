class Movie:
    def __init__(self, title, release_year, rating):
        self.title = title
        self.release_year = release_year
        self.rating = rating

    def __repr__(self):
        string_representation = f"\n{self.title} -- {self.release_year} -- {self.rating}"
        return string_representation
    
    def description(self):
        return f"{self.name} was released with a budget of ${self.budget} in {self.release_year}.It was directed by {self.director}"


