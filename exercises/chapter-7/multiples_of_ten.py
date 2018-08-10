# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
number = input('Please provide a number: ')

if int(number) % 10 == 0:
    print(number + " is a multiple of 10.")
else:
    print(number + " is not a multiple of 10.")