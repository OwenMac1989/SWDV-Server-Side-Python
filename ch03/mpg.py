#!/usr/bin/env python3

# display a welcome message
from ast import Continue


print("The Miles Per Gallon program")
print("Start ?")
LoopConditionUser = input("Y/N \t")
loopCondition = False
if LoopConditionUser.lower() == "y":
    loopCondition = True
else:
    print("Must type y to start program, otherwise please press the x on the command window.")
while loopCondition == True:
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallons = float(input("Enter cost per gallon:"))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
        continue
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
        continue
    elif cost_per_gallons <= 0:
        print("Cost must be greater than zero. Please try again.")
        continue
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        total_cost = round(gallons_used * cost_per_gallons, 2)
        cost_per_mile = round(cost_per_gallons / mpg,2)
        print("Miles Per Gallon:\t", mpg)
        print("Cost Per Mile:$\t", cost_per_mile)
        print("Total Cost:$\t", total_cost)


    LoopConditionUser = input("Would you like to calculate another one ? (Y/N)")
    if LoopConditionUser.lower() == "y":
        loopCondition = True
    else:
        loopCondition = False
    

print()
print("Bye!")



