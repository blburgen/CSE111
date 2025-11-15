""" 
    Author: Brady Burgener
"""
from datetime import datetime
import csv

""" 
    Main function
    This section runs the menu for the progam.  It loops until the user enters 0.
"""
def main():
    run_prog = True
    art_dict = {}
    art_dict = read_dictionary("art.csv", 0)
    next_key = find_next_key(art_dict)
    while run_prog:
        print(f"\nWhat would you like to do:")
        print(f"1. View available art")
        print(f"2. Add an art piece")
        print(f"3. Calculate prices for art")
        print(f"4. Search available art pieces")
        print(f"0. Quit\n")
        user_input = input(f"Your number choice: ")
        if user_input == '1':
            list_print(art_dict)
        elif user_input == '2':
            new_entry=new_art_user_input()
            write_to_file("art.csv", next_key, new_entry)
            art_dict = read_dictionary("art.csv", 0)
        elif user_input == '3':
            art_price(art_dict)
        elif user_input == '4':
            input_word = input("What would you like to search for: ")
            sorted_dict=search_dictionary(art_dict,input_word)
            list_print(sorted_dict)
        elif user_input == '0':
            run_prog = False

"""
    read_dictionary(filename, key_column_index) return dictionary
    this function brings in a csv file and creates a dictionary
"""
def read_dictionary(filename, key_column_index=0):
    file_dict = {}
    with open(filename, 'rt') as file:
        
        reader = csv.reader(file)
        
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                file_dict[key] = row_list
                
    return file_dict

""" 
    finds next dictionary key if it is an integer
    returns a int
"""
def find_next_key(dict):
    if len(dict) != 0:
        next_key = int(list(dict.keys())[-1]) + 1
    else:
        next_key = 1
    return next_key
""" 
    This function prints terminal a list of dictionary items
"""
def list_print(dict):
    name= "Art Name"
    artist= "Artist's Name"
    media= "Painting Media"
    dimension = "Painting Dimensions(inxin)"
    print(f"\nId#  {name:25}{artist:25}{media:25}{dimension:25}\n")
    for item in dict:
        print(f"{item:5}{dict[item][1]:25}{dict[item][2]:25}{dict[item][4]:25}{dict[item][5]}x{dict[item][6]}")

""" 
    This function take input from the user to generate a new item in the dictionary
    returns a list
"""
def new_art_user_input():
    art_name = input(f"\nWhat is the name of the art piece: ")
    artist_name = input(f"\nWhat is the name of the artist: ")
    artist_skill = input(f"\nAt time of creation how many years had the artist producted art: ")
    media = input(f"\nWhat is the media of the painting (watercolor,acrylic,oil,mixed media): ")
    art_width = input(f"\nWhat is the width of the painting in inches: ")
    art_height = input(f"\nWhat is the height of the painting in inches: ")
    
    return [art_name, artist_name, artist_skill, media, art_width, art_height, datetime.now()]

""" 
    write_to_file(file_name, new_row) return nothing
    writes a new entry to the csv file
"""
def write_to_file(filename, next_key, new_row):
    with open(filename, 'at', newline='') as file:
        writer = csv.writer(file)
        new_row.insert(0,next_key)
        writer.writerow(new_row)

""" 
    This function runs a menu for art pricing
    It loops until the user inputs 0
    input is the dictionary
    return nothing
"""        
def art_price(dict):
    run_cost = True
    while run_cost:
        print(f"\nSelect from the option below:")
        print(f"1. See the available painting prices")
        print(f"2. Calculate your own painting price")
        print(f"0. Go back")
        user_input = input(f"\nYour number choice: ")
        if user_input == '1':
            print_art(dict)
        elif user_input == '2':
            width_input = input(f"\nWhat is the painting width(inches): ")
            height_input = input(f"What is the painting height(inches): ")
            year_input = input(f"How many years of experience does the artist have:")
            price = calculate_art_cost(width_input,height_input,year_input)
            print(f"Your painting is worth ${price:.2f}")
        elif user_input == '0':
            run_cost = False

"""
  This function prints the available art pieces with their prices
  input dictionary
  returns nothing 
"""
def print_art(dict):
    name= "Art Name"
    artist= "Artist's Name"
    print(f"\n{name:25}{artist:25}Price\n")
    for item in dict:
        price = calculate_art_cost(dict[item][5], dict[item][6], dict[item][3])
        print(f"{dict[item][1]:25}{dict[item][2]:25}${price:10.2f}")
""" 
    calculate_art_cost(width, length, skill=0) return float
"""
def calculate_art_cost(width, length, skill=0):
    price = float(width) * float(length) * 0.5 * (float(skill) + 1)
    return price

""" 
    search_dictionary(file_dict, input_word) return sorted dictionary
"""
def search_dictionary(file_dict, input_word):
    new_dict={}
    for item in file_dict:
        lowercased_list = [line.lower() for line in file_dict[item]]
        if any(input_word.lower() in s for s in lowercased_list):
            new_dict[item] = file_dict[item]
    return new_dict
            

if __name__ == "__main__":
    main()