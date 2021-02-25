# handle error checking using try and except
# change file to use death valley date

import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)


for index, column_header in enumerate(header_row):
    print("Index:", index, "Column name:", column_header)


highs = []
dates = []
lows = []

# use enumerate function instead of hardcoding row value

tmax_index = header_row.index("TMAX")
tmin_index = header_row.index("TMIN")
date_index = header_row.index("DATE")

for row in csv_file:
    try:
        high = int(row[tmax_index])
        low = int(row[tmin_index])
        converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for  {converted_date}")
    else:
        highs.append(int(row[tmax_index]))
        lows.append(int(row[tmin_index]))
        dates.append(converted_date)


# print(highs)

# plot highs on chart

import matplotlib.pyplot as plt


# sitka

open_file2 = open("sitka_weather_2018_simple.csv", "r")
csv_file2 = csv.reader(open_file2, delimiter=",")

header_row2 = next(csv_file2)

for index, column_header in enumerate(header_row2):
    print("Index:", index, "Column name:", column_header)


highs2 = []
dates2 = []
lows2 = []

tmax_index2 = header_row2.index("TMAX")
tmin_index2 = header_row2.index("TMIN")
date_index2 = header_row2.index("DATE")
# use enumerate function instead of hardcoding row value

for row in csv_file2:
    highs2.append(int(row[tmax_index2]))
    converted_date = datetime.strptime(row[date_index2], "%Y-%m-%d")
    dates2.append(converted_date)
    lows2.append(int(row[tmin_index2]))


fig3, ax = plt.subplots(2)
ax[0].plot(dates2, highs2, c="red")
ax[0].plot(dates2, lows2, c="blue")
ax[0].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
ax[0].set_title("Sitka- Daily High and Low Temperatures - 2018", fontsize=16)
ax[0].set_xlabel("", fontsize=12)
ax[0].set_ylabel("Temperature(F)", fontsize=12)
ax[0].tick_params(axis="both", labelsize=16)

ax[1].plot(dates, highs, c="red")
ax[1].plot(dates, lows, c="blue")
ax[1].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax[1].set_title("Death Valley- Daily High and Low Temperatures - 2018", fontsize=16)
ax[1].set_xlabel("", fontsize=12)
ax[1].set_ylabel("Temperature(F)", fontsize=12)
ax[1].tick_params(axis="both", labelsize=16)
plt.show()
