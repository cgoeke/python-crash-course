# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.
filename = 'programming_poll.txt'

while True:
    print("\nEnter 'q' to exit the program.")
    reason = input("Why do you like programming? ")

    if reason == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason + "\n")