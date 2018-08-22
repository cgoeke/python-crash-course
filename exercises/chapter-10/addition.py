# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.
print("Please provide two numbers to add together!")

try:
    num_1 = input("First number: ")
    num_1 = int(num_1)
    
    num_2 = input("Second number: ")
    num_2 = int(num_2)

except ValueError:
    print("Please provide a valid number!")

else:
    sum = num_1 + num_2
    print("The sum of " + str(num_1) + " and " + str(num_2) + " is " + str(sum) + ".")