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
"""
import csv


""" 
    Reads the receipt.csv file, processes the file and displays the receipt according to the user requirements.
"""
def main():
    products_dict = read_dictionary("products.csv" ,0)
    print("All Products")
    print(products_dict)
    print("Requested Items")
    with open("request.csv","rt") as user_request:
        reader = csv.reader(user_request)
        next(reader)
        for line in reader:
            if line[0] in products_dict:
                print(f"{products_dict[line[0]][1]:15}: {line[1]} @ ${products_dict[line[0]][2]}")

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