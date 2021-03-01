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
dv_title_index = header_row.index("NAME")

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
        dv_chart_title = row[dv_title_index]


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
sitka_title_index = header_row2.index("NAME")
# use enumerate function instead of hardcoding row value

for row in csv_file2:
    highs2.append(int(row[tmax_index2]))
    converted_date = datetime.strptime(row[date_index2], "%Y-%m-%d")
    dates2.append(converted_date)
    lows2.append(int(row[tmin_index2]))
    chart_title = row[sitka_title_index]

import numpy as np

ytix = np.arange(30, 71, 10)
ytix2 = np.arange(40, 121, 20)

fig3, ax = plt.subplots(2)
ax[0].plot(dates2, highs2, c="red")
ax[0].plot(dates2, lows2, c="blue")
ax[0].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
ax[0].set_title(chart_title, fontsize=16)
# ax[0].set_xlabel("", fontsize=12)
# ax[0].set_ylabel("Temperature(F)", fontsize=12)
ax[0].tick_params(axis="both", labelsize=16)
ax[0].axes.xaxis.set_ticklabels([])
ax[0].set_yticks(ytix)

ax[1].plot(dates, highs, c="red")
ax[1].plot(dates, lows, c="blue")
ax[1].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax[1].set_title(dv_chart_title, fontsize=16)
# ax[1].set_xlabel("", fontsize=12)
# ax[1].set_ylabel("Temperature(F)", fontsize=12)
ax[1].tick_params(axis="both", labelsize=16)
ax[1].set_yticks(ytix2)
plt.xticks(rotation=45)
fig3.suptitle(
    f"Temperature comparison between {chart_title} and {dv_chart_title}", fontsize=16
)
fig3.tight_layout()
plt.show()
