
def queryUser(username):
    print(f"Welcome to Coeus {username}!")
    movie_input = input("What movie would you like to search up?")
    return movie_input

def get_movie_url(movie):
    try:
        return f"""https://api.themoviedb.org/3/search/movie?api_key=ddc5407839c0e22afe0624dd5f3f4235&language=en-US&query={movie}&page=1&include_adult=false"""
    except:
        e = sys.exc_info()[0]
        return e

movie = "Avatar"
print(get_movie_url(movie))
