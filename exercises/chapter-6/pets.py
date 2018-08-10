# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.
pets = []

bruno = {
    'animal type': 'iguana',
    'name': 'bruno',
    'owner': 'christian'
}
pets.append(bruno)

monster = {
    'animal type': 'cat',
    'name': 'monster',
    'owner': 'amy'
}
pets.append(monster)

for pet in pets:
    print("\nThis is everything I know about " + pet['owner'].title() + "'s " + pet['animal type'] + ":")
    for key, value in pet.items():
        print(key + ": " + value)