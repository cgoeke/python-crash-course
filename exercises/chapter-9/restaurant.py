# 9-1. Restaurant: Make a class called Restaurant  The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type  Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open 
# Make an instance called restaurant from your class  Print the two attributes individually, and then call both methods. 
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

print(my_restaurant.name)
print(my_restaurant.cuisine)
print("\n")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()