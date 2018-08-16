# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.
magicians = ['Houdini', 'Blaine', 'Copperfield']

def make_great(list):
    """Adds 'The Great' to each magicians name."""
    for i in range(len(magicians)):
        magicians[i] = 'The Great ' + magicians[i]

def show_magicians(list):
    """Prints magician names."""
    for magician in magicians:
        print(magician)

make_great(magicians)
show_magicians(magicians)