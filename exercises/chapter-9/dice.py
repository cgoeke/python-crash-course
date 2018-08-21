# 9-14. Dice: The module random contains functions that generate random numbers
# in a variety of ways. The function randint() returns an integer in the
# range you provide.
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""Creates a class representing a die."""
from random import randint

class Dice():
    """Initializes dice class."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Prints a random number based on number of sides."""
        number = randint(1, self.sides)
        print(number)


def roll_ten(dice):
    """Rolls provided dice 10 times."""
    for _ in range(10):
        dice.roll_die()

six_sided = Dice()
roll_ten(six_sided)

ten_sided = Dice(10)
roll_ten(ten_sided)

twenty_sided = Dice(20)
roll_ten(twenty_sided)