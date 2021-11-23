''''
Repeated String on HanckerRank
'''

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    substring_a_count = s.count('a')
    substring_length = len(s)

    full_occurences = math.floor(n / substring_length)
    partial_string_length = n % substring_length

    total_a_count = full_occurences * substring_a_count + s[:partial_string_length].count('a')
    return total_a_count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
