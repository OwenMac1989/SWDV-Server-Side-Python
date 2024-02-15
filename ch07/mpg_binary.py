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

def read_trip():
    opened_trip = [[]]
    with open("Trip.bin", "rb") as file:
        reader = pickle.load(file)
        for row in reader:
            opened_trip.append(row)
    return opened_trip

def list_trip(main_list):
    count = 0
    for i in main_list:
            for item in i:
                if count < 4:
                    if count == 3:
                        print(item, end ="\t\t|\t")
                        count += 1
                    else:
                        print(item, end ="\t|")
                        count += 1
                else:
                    print(item, end ="\t|\t")
                    count += 1
            print("\n")
            
    # with open(FILENAME, "wb") as file:
    #     pickle.dump(main_list, file)

def Append_List(opened_trip, main_list):
    temp_list = []
    for i in opened_trip:
            for item in i:
                temp_list.append(item)
            main_list.append(temp_list)
            temp_list = []
    return main_list

def main():
    # display a welcome message
    main_list = [["Entry", "Miles Driven", "Gallons Used","MPG"]]
        ## [0] Entry 1 , [0] Miles, [1] Gallons, [3] mpg
        ## [1] Entry 2 , [0] Miles, [1] Gallons, [3] mpg
    entry_counter = 0
    print("The Miles Per Gallon program")
    print()

    answer = input("Have you made a Trip CSV ?(y or n): ")
    print(answer)
    if answer.lower() == "y":
        print("Last Data:\n")
        opened_trip = read_trip()
        list_trip(opened_trip)
        main_list = Append_List(opened_trip, main_list)

    more = "y"
    while more.lower() == "y":
        print("\n")
        ## [0] Entry 1 , [1] Miles, [2] Gallons, [3] mpg
        ## [1] Entry 2 , [1] Miles, [2] Gallons, [3] mpg
        list_input = [entry_counter + 1]

        miles_driven = get_miles_driven()
        list_input.append(miles_driven)

        gallons_used = get_gallons_used()
        list_input.append(gallons_used)
                                 
        mpg = round((miles_driven / gallons_used), 2)
        list_input.append(mpg)

        main_list.append(list_input)

        entry_counter += 1

        print(f"Miles Per Gallon:\t{mpg}")

        print()

        answer = input("List Data ?(y or n)")
        if answer.lower() == "y":
            list_trip(main_list)
            
        more = input("More entries? (y or n): ")

    print("Saving to file....")
    write_trip(main_list)
    print("....Done")

    answer = input("Would you like to read any data ?(y or n): ")
    if answer.lower() == "y":
       opened_trip = read_trip()
       list_trip(opened_trip)

    print("Bye!")

if __name__ == "__main__":
    main()

