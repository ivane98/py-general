import random
import string

def generate_pass(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""

    meets_criteria = False
    has_number = False
    has_special = False

    while meets_criteria == False or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        elif special_characters:
            meets_criteria = meets_criteria and has_special

        print('lenght is',len(pwd))

    return pwd

min_length = int(input('enter min length'))
has_number = input('has number').lower() == 'y'
has_special = input('has special').lower() == 'y'
pwd = generate_pass(min_length, has_number, has_special)

print(pwd)
