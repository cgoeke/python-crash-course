# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.
magicians = ['Houdini', 'Blaine', 'Copperfield']

def show_magicians(list):
    """Prints magician names."""
    for magician in magicians:
        print(magician)

show_magicians(magicians)