# 15-9. Multiplication: When you roll two dice, you usually add the two numbers
# together to get the result. Create a visualization that shows what happens if
# you multiply these numbers instead.
import pygal

from die import Die

die_1 = Die(6)
die_2 = Die(6)

results = []

for _ in range(1000000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of multiplying two D6 1000000 times."
hist.x_labels = [str(x) for x in range(1, max_result + 1)]
hist._x_title = "Result"
hist.y_title = "Frequecy of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('multiplication.svg')