# adding dates to file

import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column name:", column_header)


highs = []
dates = []

# example
"""
somedate = '2018-07-01'
converted_date = datetime.strptime(somedate, '%Y-%m-%d')
print(converted_date)
"""

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)


# print(highs)

# plot highs on chart

import matplotlib.pyplot as plt


fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.title("Daily High Temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", labelsize=16)

fig.autofmt_xdate()
plt.show()