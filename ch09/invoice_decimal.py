#!/usr/bin/env python3


from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc
lc.setlocale(lc.LC_ALL, "en_US")
# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    subtotal = subtotal.quantize(Decimal("1.00"), ROUND_HALF_UP)
    shipping = subtotal * Decimal(0.085)
    shipping = shipping.quantize(Decimal("1.00"), ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + sales_tax + shipping

    currencyFor = ">10"
    literalFor = "20"
    form = "10,"


    # display the results
    print(f"{'Order total:':{literalFor}}{(lc.currency(order_total)):{currencyFor}}")
    print(f"{'Discount amount:':{literalFor}}{discount:{form}}")
    print(f"{'Subtotal:':{literalFor}}{subtotal:{form}}")
    print(f"{'Shipping:':{literalFor}}{shipping:{form}}")
    print(f"{'Sales tax:':{literalFor}}{sales_tax:{form}}")
    print(f"{'Invoice total:':{literalFor}}{(lc.currency(invoice_total)):{currencyFor}}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
