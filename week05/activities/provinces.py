""" 
    Author: Brady Burgener
        Open the provinces.txt file for reading.
        Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
        Print the entire list.
        Remove the first element from the list.
        Remove the last element from the list.
        Replace all occurrences of "AB" in the list with "Alberta".
        Count the number of elements that are "Alberta" and print that number.
"""

def main():
    provinces_list = []
    with open("provinces.txt", "rt") as provinces:
        for line in provinces:
            provinces_list.append(line.strip())
    print(provinces_list)
    
    provinces_list.pop(0)
    provinces_list.pop()
    
    count = 0
    
    for i, item in enumerate(provinces_list):
        if item == 'AB':
            provinces_list[i] = "Alberta"
            count += 1
        elif item.lower() == "alberta":
            count += 1
    
    countOther = provinces_list.count("Alberta")
    
    print(provinces_list)
    print(f"Alberta occurs {count} or {countOther} times in the modified list.")

if __name__ == "__main__":
    main()