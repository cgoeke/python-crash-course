# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
sandwich_orders = ['pbj', 'turkey', 'pastrami', 'meetball', 'pastrami', 'pastrami']
finished_sandwiches = []

print("We are currently out of pastrami!")
print("\n")

while 'pastrami' in sandwich_orders:
   sandwich_orders.remove('pastrami')

while sandwich_orders:
    for sandwich in sandwich_orders:
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
        print("Your " + sandwich + " sandwich has been made.")

print("\nAll sandwiches made: ")
for sandwich in finished_sandwiches:
    print("-" + sandwich)