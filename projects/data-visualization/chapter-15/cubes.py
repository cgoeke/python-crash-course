# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then plot the first 5000 cubic numbers.
import matplotlib.pyplot as plt

# First five cubic numbers
x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, edgecolor='none', s=40)

# First 5000 cubic numbers
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, edgecolor='none', s=40)

# Set chart title and label axis.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)
plt.axis([0, 5100, 0, 5100**3])

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()