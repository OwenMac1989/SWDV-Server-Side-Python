#!/usr/bin/env python3
        
from asyncio import Condition
def get_float(prompt, low_valid, high_valid):
    loopCondtion = False
    while loopCondtion == False:
        num_float = float(input(prompt))
        if num_float < low_valid or num_float > high_valid:
            print("Entry must be greater than ", low_valid," and less than or equal to  ",high_valid)
        else:
            loopCondtion = True
            return num_float

def get_int(prompt, low_valid, high_valid):
    loopCondtion = False
    while loopCondtion == False:
        num_int = int(input(prompt))
        if num_int < low_valid or num_int > high_valid:
            print("Entry must be greater than ", low_valid," and less than or equal to  ",high_valid)
        else:
            loopCondtion = True
            return  num_int

def main():
    choice = "y"
    while choice.lower() == "y":
        valid_float = get_float("Enter float: ", 0, 1000)
        print("Valid Input = ",valid_float)
        valid_integer = get_float("Enter integer: ", 0, 50)
        print("Valid Input = ",valid_integer)
        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()



    
