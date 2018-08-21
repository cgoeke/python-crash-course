# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.
class Restaurant():
    """Creates a restaurant object."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes.""" 
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant name and cuisine type."""
        print(self.name + " is a " + self.cuisine + " restaurant.")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print("We are open.")

    def set_number_served(self, number_served):
        """Sets the number of people served."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increments number of people served by amount provided."""
        self.number_served += number_served
    
my_restaurant = Restaurant("Christian's", "Thai")
served_message = my_restaurant.name + " " + my_restaurant.cuisine + " has served " 
served_message += str(my_restaurant.number_served) + " people."
print(served_message)

my_restaurant.number_served = 100
served_message = my_restaurant.name + " " + my_restaurant.cuisine + " has served " 
served_message += str(my_restaurant.number_served) + " people."
print(served_message)

my_restaurant.set_number_served(50)
served_message = my_restaurant.name + " " + my_restaurant.cuisine + " has served " 
served_message += str(my_restaurant.number_served) + " people."
print(served_message)

my_restaurant.increment_number_served(75)
served_message = my_restaurant.name + " " + my_restaurant.cuisine + " has served " 
served_message += str(my_restaurant.number_served) + " people."
print(served_message)