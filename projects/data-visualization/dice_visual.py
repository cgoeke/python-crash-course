import pygal

from die import Die

die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]


for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [str(x + 1) for x in max_result]
hist._x_title = "Result"
hist.y_title = "Frequecy of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual_.svg')