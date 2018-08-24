# 16-2. Sitka-Death Valley Comparison: The temperature scales on the Sitka
# and Death Valley graphs reflect the different ranges of the data. To accurately
# compare the temperature range in Sitka to that of Death Valley, you
# need identical scales on the y-axis. Change the settings for the y-axis on
# one or both of the charts in Figures 16-5 and 16-6, and make a direct comparison
# between temperature ranges in Sitka and Death Valley (or any two
# places you want to compare). You can also try plotting the two data sets on
# the same chart.
import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'

# Get dates, high and low temperatures from file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - Death Valley, CA 2014", fontsize=24)
# plt.xlabel(''), fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 120)

plt.show()