# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
guests = ['Christian', 'Amy', 'Mom']

message = guests[0] + ", you have been invited to dinner."
print(message)

message = guests[1] + ", you have been invited to dinner."
print(message)

message = guests[2] + ", you have been invited to dinner."
print(message)

print("\nSorry, " + guests[2] + " can't make it.")

# Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
guests.remove('Mom')
guests.append('Dad')

# Print a second set of invitation messages, one for each person who is still
# in your list.
message = "\n" + guests[0] + ", you have been invited to dinner."
print(message)

message = guests[1] + ", you have been invited to dinner."
print(message)

message = guests[2] + ", you have been invited to dinner."
print(message)