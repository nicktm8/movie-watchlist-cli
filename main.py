from services.movie_manager import MovieManager

print("-" * 50)
print("\n           Welcome to Movie Wachlist app \n")

manager = MovieManager()

running = True

while running:
    print("-" * 50)
    print("\nChoose an option:\n1.Add movie\n2.Remove movie\n3.Show all movies\n4.Exit\n")
    command  = input("Enter number 1, 2, 3 or 4: ")
    print("-" * 50)
    if command == '1':
        manager.add_movie()
            
    elif command == '2':
        manager.remove_movie()
        
    elif command == '3':
        manager.load_all_movies()
          
    elif command == '4':
        running = False
        
    else:
        print("\nWrong command.\n")
        
print("\nGoodbye!")
