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


for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for  {converted_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(converted_date)


# print(highs)

# plot highs on chart

import matplotlib.pyplot as plt


fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.title("Daily High and Low Temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", labelsize=16)

fig.autofmt_xdate()
plt.show()
