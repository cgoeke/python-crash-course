# 16-3. Rainfall: Choose any location you’re interested in, and make a visualization
# that plots its rainfall. Start by focusing on one month’s data, and then once
# your code is working, run it for a full year’s data.
import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'

# Get dates, high and low temperatures from file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Prints header
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, rainfall = [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            rain = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfall.append(rain)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfall, c='blue')

## Format plot
plt.title("Daily Precipitation - Sitka, Alaska 2014", fontsize=24)
# plt.xlabel(''), fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()