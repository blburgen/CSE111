import random

def main():
    numbers_list = [16.2, 75.1, 52.3]
    number = 5
    print(numbers_list)
    
    append_random_numbers(numbers_list)
    print(numbers_list)
    
    append_random_numbers(numbers_list,number)
    print(numbers_list)
    
    words = []
    
    append_random_words(words)
    print(words)
    
    append_random_words(words,number)
    print(words)
    

def append_random_numbers(numbers_list, quantity = 1):
    count = 0
    while count < quantity:
        numbers_list.append(round(random.uniform(0, 100),1))
        count += 1
        
def append_random_words(words_list, quantity=1):
    possibility = [
        "arm","heir","deficit","lifestyle","minute","bold","sigh","physics","writer","tourist",\
        "dominate","rank","instrument","professor","trade","hesitate","witness","weak","ignorance","muscle","morning"
    ]
    
    for _ in range(quantity):
        words_list.append(random.choice(possibility))

if __name__ == "__main__":
    main()