""" 
    Author: Brady Burgener
    
    Time Track:
        11/11/2025: 1.5hr
        11/12/2025: 1.5hr + 1.5hr
        11/12/2025: 
"""
from datetime import datetime
import csv

def main():
    run_prog = True
    art_dict = {}
    art_dict = read_dictionary("art.csv", 0)
    next_key = find_next_key(art_dict)
    while run_prog:
        print(f"\nWhat would you like to do:")
        print(f"\n1. View available art")
        print(f"\n2. Add an art piece")
        print(f"\n3. Calculate price for art")
        user_input = input(f"\n0. Quit\nYour number choice: ")
        if user_input == '1':
            list_print(art_dict)
        elif user_input == '2':
            new_entry=new_art_user_input()
            write_to_file("art.csv", next_key, new_entry)
            art_dict = read_dictionary("art.csv", 0)
        elif user_input == '3':
            art_price(art_dict)
        elif user_input == '0':
            run_prog = False

"""
    read_dictionary(filename, key_column_index) return dictionary
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

def list_print(dict):
    name= "Art Name"
    artist= "Artist's Name"
    media= "Painting Media"
    dimension = "Painting Dimensions(inxin)"
    print(f"\nId#  {name:25}{artist:25}{media:25}{dimension:25}\n")
    for item in dict:
        print(f"{item:5}{dict[item][1]:25}{dict[item][2]:25}{dict[item][4]:25}{dict[item][5]}x{dict[item][6]}")

def new_art_user_input():
    art_name = input(f"\nWhat is the name of the art piece: ")
    artist_name = input(f"\nWhat is the name of the artist: ")
    artist_skill = input(f"\nHow many years has the artist producted art: ")
    media = input(f"\nWhat is the media of the painting (watercolor,acrylic,oil,mixed media): ")
    art_width = input(f"\nWhat is the width of the painting in inches: ")
    art_height = input(f"\nWhat is the height of the painting in inches: ")
    
    return [art_name, artist_name, artist_skill, media, art_width, art_height, datetime.now()]

""" 
    write_to_file(file_name, new_row) return null
    writes a new entry to the csv file
"""
def write_to_file(filename, next_key, new_row):
    with open(filename, 'at', newline='') as file:
        writer = csv.writer(file)
        new_row.insert(0,next_key)
        writer.writerow(new_row)
        
def art_price(dict):
    run_cost = True
    while run_cost:
        print(f"\nSelect from the option below:")
        print(f"1. See the available painting prices")
        print(f"2. Calculate your own painting price")
        print(f"0. Go back")
        user_input = input(f"\nWhat is your choice?")
        if user_input == '1':
            pass
        elif user_input == '2':
            width_input = input(f"\nWhat is the painting width: ")
            height_input = input(f"What is the painting height: ")
            year_input = input(f"How many years of experience does the artist have:")
            price = calculate_art_cost(width_input,height_input,year_input)
            print(f"Your painting is worth ${price:.2f}")
        elif user_input == '0':
            run_cost = False
""" 
    calculate_art_cost(width, length, skill=0) return float
"""
def calculate_art_cost(width, length, skill=0):
    price = float(width) * float(length) * 0.1 * (float(skill) + 1)
    return price

""" 
    search_dictionary(file_dict, input_word) return list
"""
def search_dictionary(file_dict, input_word):
    pass

if __name__ == "__main__":
    main()