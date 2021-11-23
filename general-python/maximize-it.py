'''https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true'''

import itertools

# Collect inputs
K, M = list(map(int, input().split()))
print('\n ---------------------')
print(K)
print(M)

rows = [list(map(int, input().split()))[1:] for i in range(K)]
print(rows)

# First define the calculation
def score(x_list):
    sum = 0
    for X in x_list:
        sum += X**2
    
    return sum % M

# Generate a list with all X combinations
x_combinations = list(itertools.product(*rows)) # the star unpacks the rows matrix, ie. take each list in rows and feed it as argument
result = max(list(map(score, x_combinations)))

print(result)


