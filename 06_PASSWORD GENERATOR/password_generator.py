import random
import string

min_length = int(input("How long would you like the password to be? - "))
numbers = input("Do you want numbers included? (Yes/No) - ").strip().lower()
special_characters = input(
    "Do you want special characters included? (Yes/No) - ").strip().lower()


def password_generator(min_length, numbers, special_characters):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers == "yes" and special_characters == "yes":
        characters += digits + special

    elif numbers == "yes":
        characters += digits

    elif special_characters == "yes":
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers == "yes":
            meets_criteria = has_number

        if special_characters == "yes":
            meets_criteria = meets_criteria and has_special

    return pwd


pwd = password_generator(min_length, numbers, special_characters)
print(f"Your password is : {pwd} ")
