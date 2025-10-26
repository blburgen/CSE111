"""
    Author: Brady Burgener
    
    Purpose:  A program that will accept user input that describes a tire then calculate and display the tire's volume.
    Enhancements:
    added a check to see if the input is a number
    added a loop so that the user can redo the process
    ask user if they would like to buy tires and request thier number
"""
import math
from datetime import datetime

# gets the date
date = datetime.now()

# checks to see if the input is a whole number, if it is not a number it asks for whole number
def real_number(message):
    real = False
    while not real:
        function_number = input(message)
        try:
            function_number = int(function_number)
            return function_number
        except:
            print("Please put in a whole number.")

use_program = "y"

# runs the program until user does not want to run calculations
while use_program[0] == "y":
    width = real_number("Enter the width of the tire in mm (ex 205): ")
    aspect_ratio = real_number("Enter the aspect ratio of the tire (ex 60): ")
    diameter = real_number("Enter the diameter of the wheel in inches (ex 15): ")

    # Calculates the tire volume
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / (10000000000)

    print(f"The approximate volume is {volume:.2f} liters")
    
    # Asks user if they would like to buy tire and gets their phone number
    buy = input("Would you like to buy tires with the dimensions you entered (yes/no): ")
    while buy[0] != "y" and buy[0] != "n":
        print("\nPlease enter an answer:")
        buy = input("Would you like to buy tires with the dimensions you entered (yes/no)? ")
    phone_number = "xxx-xxx-xxxx"
    if buy[0] == "y":
        phone_number = input("Please enter your phone number: ")
    
    # Writes user info to volumes.txt
    with open("volumes.txt", "at") as tire_file:
        print(f"{date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone_number}", file=tire_file)
    
    # checks to see if the user would like to do another calculation
    use_program = input("Would you like to do another calculation? ")
    while use_program[0] != "y" and use_program[0] != "n":
        print("\nPlease enter an answer:")
        use_program = input("Would you like to do another calculation (yes/no)? ")