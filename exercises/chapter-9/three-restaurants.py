# 9-2. Three Restaurants: Start with your class from Exercise 9-1  Create three different instances from the class, and call      # describe_restaurant() for each instance 
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

my_restaurant = Restaurant("Christian's", "Thai")
my_restaurant.describe_restaurant()

mikes_restaurant = Restaurant("Mike's", "Pizzeria")
mikes_restaurant.describe_restaurant()

joes_restaurant = Restaurant("Tokyo", "Sushi")
joes_restaurant.describe_restaurant()