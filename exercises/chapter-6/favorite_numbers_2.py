# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.
favorite_numbers = {
    'Amy': [2, 420],
    'Christian': [7, 13, 666],
    'Mom': [13, 3, 12],
    'Dad': [42, 76],
    'Bob': [14, 18, 9]
}

for person, numbers in favorite_numbers.items():
    print("\n" + person.title() + "'s favorite numbers are:")
    for number in numbers:
        print(number)