"""A class representing a restaurant."""
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