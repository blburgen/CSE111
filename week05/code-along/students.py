import csv

def main():
    student_dict = {}
    student_dict = read_dictionary("students.csv", 0)
    
    inumber = input("Please enter I-Number (xx-xxx-xxxx): ")
    
    inumber = inumber.replace("-","")
    
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            if inumber not in student_dict:
                print("No such student")
            else:
                student = student_dict[inumber]
                name = student[1]
                
                print(name)

def read_dictionary(filename, key_column_index=0):
    file_dict = {}
    with open(filename, 'rt') as students:
        
        reader = csv.reader(students)
        
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                file_dict[key] = row_list
                
    return file_dict

if __name__ == "__main__":
    main()