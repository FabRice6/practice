import math
import os
import random
import re
import sys
import numpy as np

# Load the training data to build the model
data = open('ai/data/laptop-battery-life.txt')

x = []
y = []

for i in range(100):
    row = list(data.readline().split(','))
    # Don't consider full charges, the charging time will be larger than was needed
    # Don't consider zero charging times, it means zero battery life
    try:
        x_data = float(row[0])
    except ValueError:
        continue
    try:
        y_data = float(row[1])
    except ValueError:
        continue

    if x_data == 0 or y_data == 8:
        pass
    else:
        x.append(x_data)
        y.append(y_data)

x = np.array(x)
y = np.array(y)

# We'll assume the intercept is zero: no charging = no battery
# Thus we only need to find the average slope
slopes = np.divide(y, x)
average_slope = np.average(slopes)


if __name__ == '__main__':
    timeCharged = float(input().strip())
    print(min(8, timeCharged * average_slope))