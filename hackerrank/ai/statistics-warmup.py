"""
Example input data: 
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
"""
import numpy as np
from scipy import stats

# Collect the input data
n = int(input())
data = list(map(int, input().split()))

# Calculate the stats
mean = np.mean(data)
median = np.median(data)
mode, count = stats.mode(data)
mode = int(mode)
std = np.std(data)
lower_bound = mean - 1.96 * std / np.sqrt(n)
upper_bound = mean + 1.96 * std / np.sqrt(n)

# Print the results to STDOUT
print(f"{mean}\n{median}\n{mode}\n{std}\n{lower_bound} {upper_bound}")


