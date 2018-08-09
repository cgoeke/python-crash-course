# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
foods = ('pizza', 'pasta', 'salad', 'tacos', 'hamburgers')

# Use a for loop to print each food the restaurant offers.
print("Menu:")
for food in foods:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the
# change.
    #foods[1] = 'steak'

# The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.
foods = 'pizza', 'pasta', 'salad', 'steak', 'lasagna'

print("\nRevised Menu:")
for food in foods:
    print(food)