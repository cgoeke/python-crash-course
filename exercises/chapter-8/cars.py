# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Print the dictionary that’s returned to make sure 
# all the information was stored correctly.
def make_car(make, model, **options):
    """Creates dictionary of a car."""
    car = {}
    car['make'], car['model'] = make, model
    

    for key, value in options.items():
        car[key] = value
    
    return car

my_car = make_car('lamborghini', 'countach', color = 'red', year = 1980 )
print(my_car)