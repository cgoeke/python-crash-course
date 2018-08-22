# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.
print("\nPlease provide two numbers to add together!")
print("Type 'q' to quit.")

while True:
    try:
        num_1 = input("\nFirst number: ")
        if num_1 == 'q':
            break
        else:
            num_1 = int(num_1)

        num_2 = input("Second number: ")
        if num_2 == 'q':
            break
        else:
            num_2 = int(num_2)

    except ValueError:
        print("Please provide a valid number!")

    else:
        sum = num_1 + num_2
        print("\nThe sum of " + str(num_1) + " and " + str(num_2) + " is " + str(sum) + ".")