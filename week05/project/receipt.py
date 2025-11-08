"""
    Author: Brady Burgener
    
    The program must read two csv files, the customer's order and a product catalog. Each item in the customer's order 
    will be looked up in the product catalog to get get the current price. An order will be displayed in the terminal 
    that shows the customer's order details. Use the following details to create the program.
        Read the products inventory from the file products.csv.
        Read the customer's order from the file request.csv
        For each item in the order, look up the product in the catalog. Use the catalog information to calculate and display the order.
        Display the order receipt.
            Print a store name (you choose the name) at the top of the receipt.
            Print the list of ordered items. Include the item name, quantity ordered and price per item.
            Sum and print the number of ordered items.
            Sum and print the subtotal due.
            Compute and print the sales tax amount. Use 6% as the sales tax rate.
            Compute and print the total amount due.
            Print a thank you message.
            Get the current date and time from your computer’s operating system and print the current date and time.
            Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
            
    Enhancements:
    added alignment for the receipt
    added reminder for when our next New Years sale is
    added return by date
    
"""
import csv
from datetime import datetime, timedelta


""" 
    Reads the receipt.csv file, processes the file and displays the receipt according to the user requirements.
"""
def main():
    TAX_RATE = 0.06
    items_total = 0
    subtotal = 0
    try: 
        products_dict = read_dictionary("products.csv" ,0)
        # print("All Products")
        # print(products_dict)
        print("-----Brady's Groceries-----")
        with open("request.csv","rt") as user_request:
            reader = csv.reader(user_request)
            next(reader)
            for line in reader:
                print(f"{products_dict[line[0]][1]:15}: {line[1]} @ ${products_dict[line[0]][2]}")
                items_total += int(line[1])
                subtotal += int(line[1]) * float(products_dict[line[0]][2])
        print(f"Number of Items: {items_total}")
        print(f"Subtotal       : ${subtotal:.2f}")
        tax = subtotal * TAX_RATE
        total = tax + subtotal
        print(f"Sales Tax      : ${tax:.2f}")
        print(f"Total:         : ${total:.2f}")
        print("Thank you for shopping at Brady's Groceries")
        print()
        print(datetime.now().strftime("%c"))
        nextyear = int(datetime.now().year) + 1
        datetime1 = datetime(nextyear,1,1)
        datetime2 = datetime.now()
        datereturn = datetime2 + timedelta(30)
        days_to_sell = datetime1 - datetime2
        print()
        print(f"***{days_to_sell.days} days to our New Years Sale***")
        print()
        print(f"Returns Due By: 9:00PM {datereturn.strftime("%x")}")
    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file: ", key_err)
    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)
    except PermissionError as perm_err:
        print(perm_err)
        

""" 
    Parameters
        filename,key_column_index
    Return Type
        Dictionary
    This function reads the product data from the csv file passed to the function in the filename parameter. 
    The dictionary key is contained in the csv data column indicated by the key_column_index parameter, the 
    value of each dictionary item is the list derived from the values in the row of the csv file. Function 
    returns a dictionary of products.
"""
def read_dictionary(filename, index_location):
    file_dict = {}
    with open(filename, 'rt') as fileName:
        reader = csv.reader(fileName)
        
        next(reader)
        for line in reader:
            key = line[index_location]
            file_dict[key] = line
        
    return file_dict

if __name__ == "__main__":
    main()