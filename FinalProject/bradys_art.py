""" 
    Author: Brady Burgener
    
    Time Track:
        11/11/2025: 1.5hr
        11/12/2025: 1.5hr + 1hr
        11/12/2025: 
"""
import datetime
import csv


def main():
    art_dict = {}
    art_dict = read_dictionary("art.csv", 0)
    print(art_dict)
    next_key = find_next_key(art_dict)
    print(next_key)
    new_entry=['not me',"Brady Burgener",0, "Oil"]
    write_to_file("art.csv", next_key, new_entry)

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

""" 
    write_to_file(file_name, new_row) return null
    writes a new entry to the csv file
"""
def write_to_file(filename, next_key, new_row):
    with open(filename, 'at', newline='') as file:
        writer = csv.writer(file)
        new_row.insert(0,next_key)
        writer.writerow(new_row)
        

""" 
    calculate_art_cost(width, length, skill=0) return float
"""
def calculate_art_cost(width, length, skill=0):
    pass

""" 
    search_dictionary(file_dict, input_word) return list
"""
def search_dictionary(file_dict, input_word):
    pass

if __name__ == "__main__":
    main()