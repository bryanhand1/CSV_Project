# import modules needed
import csv
from datetime import datetime

# Open the needed files
open_file = open("sitka_weather_2018_simple.csv", "r")
sitka_file = csv.reader(open_file, delimiter=",")

open_file2 = open("death_valley_2018_simple.csv", "r")
dv_file = csv.reader(open_file2, delimiter=",")


sitka_header_row = next(sitka_file)
dv_header_row = next(dv_file)

# Enumerate Both Files to find index values of each row
for index, column_header in enumerate(sitka_header_row):
    print(index, column_header)

for index, column_header in enumerate(dv_header_row):
    print(index, column_header)

# Extract the high and low values from each file

# Sitka Values
sitka_highs = []
sitka_dates = []
sitka_lows = []


for row in sitka_file:
    sitka_highs.append(int(row[sitka_header_row.index("TMAX")]))
    sitka_lows.append(int(row[sitka_header_row.index("TMIN")]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    sitka_dates.append(converted_date)
    sitka_station = str(row[sitka_header_row.index("NAME")])

# Death Valley Values
dv_highs = []
dv_dates = []
dv_lows = []

for row in dv_file:
    try:
        high = int(row[dv_header_row.index("TMAX")])
        low = int(row[dv_header_row.index("TMIN")])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        dv_highs.append(high)
        dv_lows.append(low)
        dv_dates.append(converted_date)
        dv_station = str(row[dv_header_row.index("NAME")])

# Create Dual Plot
import matplotlib.pyplot as plt

# fig, ax = plt.subplots(2,2)  -  this will create a visualization with 2 charts on it

fig, ax = plt.subplots(2)

# Set Main title
plt.suptitle(f"Temperature comparison between {sitka_station} and {dv_station}")


# First plot of Sitka Valley
ax[0].plot(sitka_dates, sitka_highs, c="red")
ax[0].plot(sitka_dates, sitka_lows, c="blue")

fig.autofmt_xdate()

ax[0].fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor="blue", alpha=0.1)


ax[0].set_title(f"{sitka_station}")

# Second Plot of Death Valley

ax[1].plot(dv_dates, dv_highs, c="red")
ax[1].plot(dv_dates, dv_lows, c="blue")

fig.autofmt_xdate()

ax[1].fill_between(dv_dates, dv_highs, dv_lows, facecolor="blue", alpha=0.1)

ax[1].set_title(f"{dv_station}")

# Plot Formatting

plt.show()
