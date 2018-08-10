# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
people = []

person = {
    'first_name': 'Christian',
    'last_name': 'Goeke',
    'age': 37,
    'city': 'San Diego'
}
people.append(person)

person = {
    'first_name': 'Amy',
    'last_name': 'Fernandez',
    'age': 35,
    'city': 'San Diego'
}
people.append(person)

person = {
    'first_name': 'Glen',
    'last_name': 'Goeke',
    'age': 65,
    'city': 'St. Louis'
}
people.append(person)

for person in people:
    name = person['first_name'] + " " + person['last_name']
    age = str(person['age'])
    city = person['city']

    print("\nName: " + name + 
        "\nAge: " + age + 
        "\nCity: " + city)