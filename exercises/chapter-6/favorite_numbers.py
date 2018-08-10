# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
favorite_numbers = {
    'Amy': 2,
    'Christian': 7,
    'Mom': 13,
    'Dad': 42,
    'Bob': 14
}

number = favorite_numbers['Amy']
print("Amy's favorite number is " + str(number) + ".")

number = favorite_numbers['Christian']
print("Christian's favorite number is " + str(number) + ".")

number = favorite_numbers['Mom']
print("Mom's favorite number is " + str(number) + ".")

number = favorite_numbers['Dad']
print("Dad's favorite number is " + str(number) + ".")

number = favorite_numbers['Bob']
print("Bob's favorite number is " + str(number) + ".")