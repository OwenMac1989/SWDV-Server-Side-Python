#!/usr/bin/env python3
        
from asyncio import Condition
import validation as valid
# def get_float(prompt, low_valid, high_valid):
#     num_float = float(input(prompt))
#     loopCondtion = False
#     while loopCondtion == False:
#         if num_float < low_valid or num_float > high_valid:
#             print("Entry must be greater than % and less than or equal to % "%(low_valid, high_valid))
#         else:
#             loopCondtion = True
#             return num_float

# def get_int(prompt, low_valid, high_valid):
#     num_int = int(input(prompt))
#     loopCondtion = False
#     while loopCondtion == False:
#         if num_int < low_valid or num_int > high_valid:
#             print("Entry must be greater than % and less than or equal to % "%(low_valid, high_valid))
#         else:
#             loopCondtion = True
#             return  num_int

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = valid.get_float(prompt="Enter Monthly Investment\t", low_valid= 0, high_valid= 1000)
        yearly_interest_rate = valid.get_float(prompt="Enter Yearly Interest Rate\t", low_valid= 0, high_valid= 15)
        years = valid.get_int(prompt="Enter Years\t\t", low_valid= 0, high_valid= 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print(f"Future value:$\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()



    
