# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.
def city_country(city, country):
    """Returns a formatted city and country."""
    return city.title() + ", " + country.title()

st_louis = city_country('st. louis', 'america')
print(st_louis)

tokyo = city_country('tokyo', 'japan')
print(tokyo)

berlin = city_country('berlin', 'germany')
print(berlin)