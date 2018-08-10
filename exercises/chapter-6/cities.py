# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    'san diego': {
        'country': 'united states',
        'population': 1407000,
        'fact': 'Ronald Reagan was the first person to drive across the Coronado Bridge when it opened in 1969.'
    },
    'tokyo': {
        'country': 'japan',
        'population': 5240000000,
        'fact': 'the city is the largest metropolitan area in the world.'
    },
    'st. louis': {
        'country': 'united states',
        'population': 311404,
        'fact': 'peanut butter was invented here.'
    }
}

for city, info in cities.items():
    print("\nHere is all the information available for " + city.title() + ":")
    for key, value in info.items():
        if key == 'country':
            value = value.title()
        if key == 'population':
            value = str(value)  
        print(key.title() + ": " + value)