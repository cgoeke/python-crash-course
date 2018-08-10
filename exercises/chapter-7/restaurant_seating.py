# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.
group_size = input("How many people are in the dinner group? ")
group_size = int(group_size)

if group_size > 8:
    print("Please wait for the next available table.")
else:
    print("Your table is ready.") 