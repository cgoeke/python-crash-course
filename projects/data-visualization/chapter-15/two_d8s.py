# 15-7. Two D8s: Create a simulation showing what happens if you roll two eightsided
# dice 1000 times. Increase the number of rolls gradually until you start to
# see the limits of your system’s capabilities.
import pygal

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []

for _ in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling two D8 1000000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist._x_title = "Result"
hist.y_title = "Frequecy of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('two_d8s_.svg')

