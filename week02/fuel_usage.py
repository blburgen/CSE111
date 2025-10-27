""" 
    Write a Python program that asks the user for three numbers:

    A starting odometer value in miles
    An ending odometer value in miles
    An amount of fuel in gallons
    Your program must calculate and print fuel efficiency in both miles per gallon and liters per 100 kilometers. 
    Your program must have three functions named as follows:

    main
    miles_per_gallon
    lp100k_from_mpg
    All user input and printing must be in the main function. In other words, the miles_per_gallon and lp100k_from_mpg 
    functions must not call the the input or print functions.
    
    Enhancements:
    created a function to verify the input numbers are correct
"""

def main():
    start_odometer = valid_number("What is your starting odometer value in miles: ", "whole", int)
    end_odometer = valid_number("What is your ending odometer value in miles: ", "whole", int)
    gallons = valid_number("What is the amount of fuel in gallons used: ", "decimal", float)
    
    mpg = miles_per_gallon(start_odometer, end_odometer, gallons)
    print(f"{mpg:.1f} miles per gallon")
    
    lpk = lp100k_from_mpg(mpg)
    print(f"{lpk:.2f} liters per 100 kilometers")
    
def valid_number(prompt, word, value):
    input_value = -1
    while input_value < 0:
        try:
            input_value = value(input(prompt))
            if input_value < 0:
                print(f"Please input a positive {word} number")
        except:
            print(f"Please input a positive {word} number")
    return input_value
    
def miles_per_gallon(first, second, gallons):
    return ((second - first) / gallons)
    

def lp100k_from_mpg(mpg):
    return (235.215/mpg)
    

main()