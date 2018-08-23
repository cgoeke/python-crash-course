# 15-8. Three Dice: If you roll three D6 dice, the smallest number you can roll is 3
# and the largest number is 18. Create a visualization that shows what happens
# when you roll three D6 dice.
import pygal

from die import Die

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

results = []

for _ in range(1000000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling three D6 1000000 times."
hist.x_labels = [str(x) for x in range(3, max_result + 1)]
hist._x_title = "Result"
hist.y_title = "Frequecy of Result"

hist.add('D6 * 3', frequencies)
hist.render_to_file('three_dice.svg')