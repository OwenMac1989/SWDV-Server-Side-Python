#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallons = float(input("Enter cost per gallon:\t"))

# calculate miles per gallon
# mpg = miles_driven / gallons_used # old logic
mpg = round(miles_driven / gallons_used, 1)
total_cost = round(gallons_used * cost_per_gallons, 2)
cost_per_mile = round(cost_per_gallons / mpg,2)
            
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Cost Per Mile:\t\t\t${cost_per_mile}")
print(f"Total Cost:\t\t\t${total_cost}")
print()
print("Bye!")


