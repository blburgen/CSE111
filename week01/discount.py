"""
    Author: Brady Burgener
    
    Purpose: Calculate the customer discoutn on Tuesday and Wednesday for a retail store.
    Enhancements:
        Add code to your program that the computer will execute if today is Tuesday or Wednesday 
        and the customer is not purchasing enough to receive the discount. This added code should 
        compute and print the difference between $50 and the subtotal which is the additional amount 
        the customer would need to purchase in order to receive the discount.
        
        Add code to your program that the computer will execute if today is not Tuesday or Wednesday.
        This added code should print to come on Tuesday or Wednesday to receive a discount
        
        Near the beginning of your program replace the code that asks the user for the subtotal with 
        a loop that repeatedly asks the user for a price and a quantity and computes the subtotal. 
        This loop should repeat until the user enters "0" for the quantity.
"""

from datetime import datetime
TUES = 1
WED = 2
SALES_TAX_RATE = 0.06

# Ask user for the subtotal
#subtotal = float(input("Please enter the subtotal: "))

print("Enter the price and quantity for each item. (enter 0 for price to exit)")
price = 1
subtotal = 0
while price != 0:
    price = float(input("Please enter the price: $"))
    if price != 0:
        quantity = int(input("Please enter the quantity: "))
        subtotal += price * quantity
        print()
        
subtotal = round(subtotal,2)
print(f"Subtotal: ${subtotal:.2f}")
print()
# Get the day of the week

day = datetime.now().weekday()

# Compute and print the discount amount
discount = 0
if subtotal >= 50:
    if day == TUES or day == WED :
        discount = 0.1
        print(f"Discount Amount: ${subtotal*discount:.2f}")
    else:
        difference = 50 - subtotal
        print(f"Purchase ${difference:.2f} more to recieve a discount")
else:
    print(f"Come back Tuesday or Wednesday for a 10% discount" )
    
# Compute and print the sales tax amount
sales_tax = subtotal * (1 - discount) * SALES_TAX_RATE
print(f"Sales Tax: ${sales_tax:.2f}")

# Compute and print the total amount due
total = subtotal * (1 - discount) + sales_tax
print(f"Total Due: ${total:.2f}")