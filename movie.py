class Movie:

	def __init__(self, title, release_year, budget, director, duration, rating):
		self.title = title
		self.release_year = release_year
		self.budget = budget
		self.director = director
		self.duration = duration
                self.rating = rating

	def description(self):
		return f"{self.name} was released with a budget of 
            ${self.budget} in {self.release_year}.
            It was directed by {self.director}"


