# 15-3. Molecular Motion: Modify rw_visual.py by replacing plt.scatter() with
# plt.plot(). To simulate the path of a pollen grain on the surface of a drop of
# water, pass in the rw.x_values and rw.y_values, and include a linewidth argument.
# Use 5000 instead of 50,000 points.
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
# Make a random walk, and plot the points.
    rw = RandomWalk(num_points=5000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)
        
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100, zorder=2)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break