# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print("\nThe " + river.title() + " runs through " + country.title() + ".")

print("\nThe following rivers are contained in this dictionary:")
for river in rivers:
    print("-" + river.title())

print("\nThe following countries are contained in this dictionary:")
for river in rivers.values():
    print("-" + river.title())