#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    pair_distances = []
    # Write your code here
    for i, element in enumerate(a):
        if i == len(a) - 1:
            break
        if element in a[i+1:]:
            distance = a[i+1:].index(element) + 1
            pair_distances.append(distance)
    
    if len(pair_distances) == 0:
        return -1
    else:
        return min(pair_distances)
        

if __name__ == '__main__':
    a = [1, 1]
    print(minimumDistances(a))
