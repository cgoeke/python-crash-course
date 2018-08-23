# 15-2. Colored Cubes: Apply a colormap to your cubes plot.
import matplotlib.pyplot as plt

# First 5000 cubic numbers
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.BuPu,
    edgecolor='none', s=40)

# Set chart title and label axis.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)
plt.axis([0, 5100, 0, 5100**3])

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()