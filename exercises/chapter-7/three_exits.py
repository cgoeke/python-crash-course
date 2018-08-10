# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
prompt = "\nWhat toppings would you like on your pizza? "
prompt += "\n(enter quit to exit): "
quit = False

while not quit: 
    pizza_toppings = input(prompt)
    if pizza_toppings == 'quit':
        quit = True
    else:
        print("Adding " + pizza_toppings + " to your pizza.")
        
# • Use a break statement to exit the loop when the user enters a 'quit' value.
while True: 
    pizza_toppings = input(prompt)
    if pizza_toppings == 'quit':
        break
    else:
        print("Adding " + pizza_toppings + " to your pizza.")