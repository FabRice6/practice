# break = Abort mission, stop the loop completely
# continue = Skip this step of the loop, but continue the loop
# pass = Be pass-ive and do nothing

import numpy as np
import pandas as pd
import math

wave = 4

top_row = [[-wave, col] for col in range(-wave, wave+1)]
bottom_row = [[wave, col] for col in range(-wave, wave+1)]
left_row = [[row, -wave] for row in range(-wave+1, wave)]
right_row = [[row, wave] for row in range(-wave+1, wave)]

directions = top_row + bottom_row + left_row + right_row

zeros = np.zeros((2*wave+1, 2*wave+1))

# print(zeros)

for position in directions:
    zeros[wave + position[0]][wave + position[1]] = 1

# print(zeros)

# print('TOP')
# print(top_row)
# print('BOTTOM')
# print(bottom_row)
# print('LEFT')
# print(left_row)
# print('RIGHT')
# print(right_row)
print('ALL')
print(directions)

bot_r, bot_c = 0, 0
# distances = sorted(directions, key=lambda k: abs(k[0]-bot_r) + abs(k[1]-bot_c))

# print(distances)

print(directions.sort(key = lambda k: (k[0] - bot_r)**2 + (k[1] - bot_c)**2))

row = [ '-', '-', '-', 'd', '-', '-']

if 'd' in row:
    print(row.index('d'))
else:
    print('not in list')

a = [1,3,2]

a.sort()

print(a)

data = { 
    'Country': [ 'Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels' , 'New Delhi', 'Brasilia'],
    'Population': [11190846, 1303171035, 207847528]
}

df = pd.DataFrame(data)

print(df.loc[1])

df.index = ['een', 'twee', 'drie']

print(df.min())

ftn = lambda x: x*2

df2 = df.applymap(ftn)

print(df2)

s ='akbdk'
n = 9

print(s.count('a'))


morse_code = '  hello ik ben fabrice'

for char in morse_code:
    print(char)
    if char == ' ':
        morse_code = morse_code[1:]
    else:
        break

print(morse_code)
