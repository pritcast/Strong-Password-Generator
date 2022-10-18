# Strong Password Generator


# Importing Module
import random
import string

# Get all the letters, numbers, symbols
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Concatinate all the letters, numbers and symbols
characters = letters+numbers+symbols

# Create an empty string to store our password
password = ""

# Take user input of no of characters
no_of_characters = int(input("Enter the number of characters: "))

# Iterate over a number of range and choose a random character in every iteration and update the password string 

for i in range(no_of_characters):
    random_ch = random.choice(characters)
    password += random_ch


# Print The Password
print(f"Your password could be: {password}")
