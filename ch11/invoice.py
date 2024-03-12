#!/usr/bin/env python3

from datetime import datetime, timedelta, date

def get_invoice_date():
    again = "y"
    while again.lower() == "y":
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")
        if invoice_date_str.find(" ") != -1:
            print("No spaces allowed")
        try:
            invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%Y")
            if datetime.now() <= invoice_date :
                print(" Invoice Date must not be greated than todays date.")
            else:
                again = "N"
        except ValueError:
            print("Must follow (MM/DD/YYYY)")
    else:
        return invoice_date
def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        invDay = invoice_date.day
        invMon = invoice_date.month
        invYear = invoice_date.year
        invDate = date(invYear, invMon, invDay)
        due_date = invDate + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
