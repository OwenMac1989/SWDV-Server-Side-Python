#!/usr/bin/env python3
import pickle
import csv
import datetime
from sqlite3 import Date

# from ch08.movies2 import FILENAME
current_time = datetime.datetime.now()


def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def write_Milege(main_list):
        with open("Trip.bin", "wb") as file:
            pickle.dump(main_list, file)

        
def main():
    # display a welcome message
    main_list = [["Entry", "Miles Driven", "Gallons Used","MPG"]]
        ## [0] Entry 1 , [0] Miles, [1] Gallons, [3] mpg
        ## [1] Entry 2 , [0] Miles, [1] Gallons, [3] mpg
    entry_counter = 0
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":
        ## [0] Entry 1 , [1] Miles, [2] Gallons, [3] mpg
        ## [1] Entry 2 , [1] Miles, [2] Gallons, [3] mpg
        list_input = [entry_counter + 1]

        miles_driven = get_miles_driven()
        list_input.append(miles_driven) # type: ignore

        gallons_used = get_gallons_used()
        list_input.append(gallons_used) # type: ignore
                                 
        mpg = round((miles_driven / gallons_used), 2)
        list_input.append(mpg) # type: ignore

        main_list.append(list_input) # type: ignore

        entry_counter += 1

        print(f"Miles Per Gallon:\t{mpg}")

        print()
        more = input("More entries? (y or n): ")

    for i in main_list:
            for item in i:
                print(item, end =" | ")
            print("\n")

    print("Saving to file....")

    write_Milege(main_list)

    print("....Done")
    
    print("Bye!")

if __name__ == "__main__":
    main()

