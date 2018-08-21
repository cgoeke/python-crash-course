# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.
class Restaurant():
    """Creates a restaurant object."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes.""" 
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Prints restaurant name and cuisine type."""
        print(self.name + " is a " + self.cuisine + " restaurant.")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print("We are open.")


class IceCreamStand(Restaurant):
    """Creates a child class of Restaurant."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Chocolate', 'Vanilla', 'Strawberry']

    def display_flavors(self):
        """Displays all ice cream flavors."""
        for flavor in self.flavors:
            print(flavor)


my_stand = IceCreamStand("Christian's")
my_stand.display_flavors()