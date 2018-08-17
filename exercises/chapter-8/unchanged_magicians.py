# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.
magicians = ['Houdini', 'Blaine', 'Copperfield']

def make_great(magicians):
    """Adds 'The Great' to each magicians name."""
    great_magicians = []

    while magicians:
        great_magician = magicians.pop()
        great_magicians.append('The Great ' + great_magician)
    
    return great_magicians

def show_magicians(magicians):
    """Prints magician names."""
    for magician in magicians:
        print(magician)

show_magicians(magicians)

great_magicians = make_great(magicians[:])
show_magicians(great_magicians)