from ast import While
from asyncio.windows_events import NULL
import csv
import sys

FILENAME = "movies.csv"

def exit_program():
    print("Terminating program.")
    sys.exit()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        # print(f"Could not find {FILENAME} file.")
        # exit_program()
        return movies
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    try:
        # raise BlockingIOError
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
    
def add_movie(movies):
    userInput = "N"
    while userInput.lower() == "n":
        name = input("Name: ")
        if name == "" or name == NULL:
            print("Invalid name try again!")
            continue
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Invalid number")
            continue
        if year < 0 :
            print("Invalid year, must be greater than 0!")
            continue
        userInput = "y"
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    movies = read_movies()
    while True:
        display_menu()        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
