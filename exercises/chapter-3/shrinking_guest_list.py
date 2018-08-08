# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
#   Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
guests = ['Christian', 'Amy', 'Dad']

message = "\n" + guests[0] + ", you have been invited to dinner."
print(message)

message = guests[1] + ", you have been invited to dinner."
print(message)

message = guests[2] + ", you have been invited to dinner."
print(message)

print("\n A bigger dinner table has been found!")

guests.insert(0, 'Jody')

guests.insert(len(guests) // 2, 'Ivaylo')

guests.append('Mom')

message = "\n" + guests[0] + ", you have been invited to dinner."
print(message)

message = guests[1] + ", you have been invited to dinner."
print(message)

message = guests[2] + ", you have been invited to dinner."
print(message)

message = "\n" + guests[3] + ", you have been invited to dinner."
print(message)

message = guests[4] + ", you have been invited to dinner."
print(message)

message = guests[5] + ", you have been invited to dinner."
print(message)

message = "\nThe table will not be ready in time :( \nWe only have room for two people."
print(message)

# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
name = guests.pop()
message = "\nSorry, " + name + " but we cannot invite you to dinner."

print(message)

name = guests.pop()
message = "Sorry, " + name + " but we cannot invite you to dinner."

print(message)

name = guests.pop()
message = "Sorry, " + name + " but we cannot invite you to dinner."

print(message)

name = guests.pop()
message = "Sorry, " + name + " but we cannot invite you to dinner."

print(message)

# Print a message to each of the two people still on your list, letting them
# know they’re still invited.
message = "\n" + guests[0] + " you are still invited to dinner."
print(message)

message = guests[1] + " you are still invited to dinner."
print(message)

# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.
del guests[:]

print(guests)