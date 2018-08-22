# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.
import json

filename = 'fav_number.json'

try:
    with open(filename) as file_object:
        fav_num = json.load(file_object)

except FileNotFoundError:
    fav_num = input("Please enter your favorite number: ")
    with open(filename, 'w') as file_object:
        json.dump(fav_num, file_object)

else:
    print("I know your favorite number! It's " + fav_num + ".")

