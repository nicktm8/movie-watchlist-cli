import os
import pickle

class FileHandler:
    
    def __init__(self):
        self.file_path = 'data/library.pkl'
        
    def file_save(self, movies):
        os.makedirs('data', exist_ok=True)
        with open(self.file_path, 'wb') as file:
            pickle.dump(movies, file)
    
    def file_load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as file:
                return pickle.load(file)
        return []
