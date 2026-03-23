from storage.file_handler import FileHandler
from models.movie import Movie

class MovieManager:
    
    def __init__(self):
        self.file_handler = FileHandler()
        self.movies = self.file_handler.file_load()
    
    def add_movie(self):
        movie_title = input("Movie title:")
        movie_release_year = input("Movie release year:")
        movie_release_year = int(movie_release_year)
        movie_genre = input("Movie genre:")
        movie_IMDb = input("Movie IMDb URL:")
        
        
        movie = Movie(movie_title, movie_release_year, movie_genre, movie_IMDb)
        
        self.movies.append(movie)
        
        self.file_handler.file_save(self.movies)
        
        print(f"\nYou have added new movie.\n")
    
    def load_all_movies(self):
        if(len(self.movies) == 0):
            print('\nNo movies.\n')
        else:
            print("\nAll movies in the watchlist:")
                
            for movie in self.movies:
                print(movie)
                print("--------")
    
    def remove_movie(self):
        self.load_all_movies()
        index = input("\nEnter the movie number you want to delete?\n")
        index = int(index) - 1
        if (0 <= index) and (index < len(self.movies)):
            self.movies.remove(self.movies[index])
            self.file_handler.file_save(self.movies)
            print('\nMovie removed.\n')
        else:
            print('\nMovie does not exists.\n')
