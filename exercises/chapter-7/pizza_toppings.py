# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
prompt = "\nWhat toppings would you like on your pizza? "
prompt += "\n(enter quit to exit): "
quit = False

while not quit: 
    pizza_toppings = input(prompt)
    if pizza_toppings == 'quit':
        quit = True
    else:
        print("Adding " + pizza_toppings + " to your pizza.")
        