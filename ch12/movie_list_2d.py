#!/usr/bin/env python3

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        count = 0 
        for i in movie_list:
            movie = i["name"]
            year = i["year"]
            count += 1
            print(f"Movie {count}: ")
            print(f"Name: {movie}")
            print(f"Year: {year} \n")
        print()

def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = {"name": name, "year": year}
    movie_list.append(movie)
    index = len(movie_list)
    valid = movie_list[index - 1]["name"]
    print(f"{valid} was added.\n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        valid = movie_list[number-1]["name"]
        movie = movie_list.remove(movie_list[number-1])
        print(f"{valid} was deleted.\n")

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    
        
def main():
    movie_list = [
            {"name" : "Monty Python and the Holy Grail",
             "year" : 1975},
            {"name" : "On the Waterfront", 
             "year" : 1954},
            {"name" : "Cat on a Hot Tin Roof",
             "year" : 1958}
    ]
    
    display_menu()
    
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
