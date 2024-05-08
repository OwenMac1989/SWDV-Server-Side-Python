#!/usr/bin/env/python3

import db
from objects import Movie

def display_title():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("minutes - View movies by minutes")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()

def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def display_movies_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())
    
def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

def display_movies_by_minutes():
    minutes = int(input("Minutes: "))
    print()
    movies = db.get_movies_by_minutes(minutes)
    display_movies(movies, str(minutes))

def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:        
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)    
        print(name + " was added to database.\n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    movie = get_movie(movie_id)
    print("You have selected:")
    for i in movie:
        print(f"{i}")
    user_input = input("Are you sure you want to Delete the Movie? (y/n)")
    if user_input.lower() == "y":
        db.delete_movie(movie_id)
        print("Movie ID " + str(movie_id) + " was deleted from database.\n")
    else:
        print("Movie was not deleted, returning to menu.")
          
def main():
    db.connect()
    display_title()
    display_categories()
    while True:        
        command = input("Command: ")
        if command.lower() == "cat":
            display_movies_by_category()
        elif command.lower() == "year":
            display_movies_by_year()
        elif command.lower() == "minutes":
            display_movies_by_minutes()
        elif command.lower() == "add":
            add_movie()
        elif command.lower() == "del":
            delete_movie()
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
