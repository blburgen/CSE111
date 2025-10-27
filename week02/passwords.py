""" 
    Author: Brady Burgener
    
    Purpose:  You are a junior software developer working for a cellular phone service provider. 
    Your company employs hundreds of workers ranging from customer support to cell tower engineers. 
    The security team has recently discovered a breach of security that they attribute to users using 
    easy to guess passwords. To help train users to create better passwords, management has asked your 
    team to create a password strength checker. This tool will allow employees to get feedback on the 
    strength of their passwords.
    Enhancements:
    
"""
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]


""" 
    Provides the user input loop. The loop asks the user for a password to test. If that password is 
    anything but "q" or "Q" call the password_strength function and report the results to the user. 
    If the user enters "q" or "Q", quit the program.
"""
def main():
    password = ""
    while password.lower() != "q":
        password = input("Please enter the password you would like to test (q or Q to quit): ")
        if password.lower() == "q":
            break
        strength = password_strength(password,10,15)
               
        print(f"{password} has a password strength of {strength}.")
        
    # with open("toppasswords.txt", "r",encoding="utf-8") as toppasswords:
    #     lines = toppasswords.readlines()
    
    # for line in lines:
    #     line.strip()

"""
    This function reads a file (specified by the filename parameter) in which each line of the file contains a single word. 
    If the word passed in the word parameter matches a word in the file the function returns a true otherwise it returns a false. 
    If the parameter case_sensitive is true a case sensitive match is performed. If case_sensitive is false a case insensitive 
    match is performed. The case_sensitive parameter should default to False 
    return Boolean
"""
def word_in_file(word,filename,case_sensitive):
    pass       
 
""" 
    This function loops through each character in the string passed in the word parameter to see if that character is in the list 
    of characters passed in the character_list parameter. If any of the characters in the word are present in the character list 
    return a true, If none of the characters in the word are in the character list return false 
    return Boolean
"""  
def word_has_character(word,character_list):
    pass

""" 
    This function creates a numeric complexity value based on the types of characters the word parameter contains. One point of 
    complexity is given for each type of character in the word. The function calls the word_has_character function for each of the 
    4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a point is added to complexity 
    rating. Since there are 4 kinds of characters the complexity rating will range from 0 to 4. (0 would be returned only if word 
    contained no characters or only contains characters that are not in any of the lists.)
    return integer
"""
def word_complexity(word):
    pass

""" 
    This function checks length requirements, checks dictionary and known-passwords, calls word_complexity to calculate the word's 
    complexity then determines the password's strength based on the user requirements. It should print the messages defined in the 
    requirements and return the password's strength as a number from 0 to 5. The min_length parameter should have a default value 
    of 10. The strong_length parameter should have a default value of 16
    return integer
"""
def password_strength(password,min_length,strong_length):
    pass

if __name__ == "__main__":
    main()