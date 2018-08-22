# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate program
# that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”
import json

filename = 'fav_number.json'

def get_num():
    """Gets favorite number from user."""
    fav_num = input("Please enter your favorite number: ")
    with open(filename, 'w') as file_object:
        json.dump(fav_num, file_object)

def read_num():
    """Prints user's favorite number."""
    with open(filename) as file_object:
        fav_num = json.load(file_object)
        print("I know your favorite number! It's " + fav_num + ".")


get_num()
read_num()