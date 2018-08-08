# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
#   Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
guests = ['Christian', 'Amy', 'Dad']

message = "\n" + guests[0] + ", you have been invited to dinner."
print(message)

message = guests[1] + ", you have been invited to dinner."
print(message)

message = guests[2] + ", you have been invited to dinner."
print(message)

print("\n A bigger dinner table has been found!")

# Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'Jody')

# Use insert() to add one new guest to the middle of your list.
guests.insert(len(guests) // 2, 'Ivaylo')

# Use append() to add one new guest to the end of your list.
guests.append('Mom')

# Print a new set of invitation messages, one for each person in your list.
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