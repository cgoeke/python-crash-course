import pygal

from die import Die

d6 = Die()

# Make some rolls and store the results in a list.
results = [d6.roll() for _ in range(1000)]

# Analyze the results
frequencies = []

for value in range(1, d6.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(1, d6.num_sides + 1)]
hist._x_title = "Result"
hist.y_title = "Frequecy of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual_.svg')