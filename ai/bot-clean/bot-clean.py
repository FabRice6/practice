"""
Note: This solution works, but code is too heavy for what it is + HackerRank will input the grid each time so also initiate the search each time.

See other solution.

Hackerrank assigment: https://www.hackerrank.com/challenges/botclean
"""
import numpy as np

def next_move(posr, posc, board):
    grid.clean()
    print(np.array(grid.grid))

class Grid(object):

    def __init__(self, grid, bot_r, bot_c):
        self.grid = grid
        self.bot_r = bot_r
        self.bot_c = bot_c
        self.bot_marker = 'b'
        self.dirt_marker = 'd'
        self.clean_marker = '-'
        self.dirt_r = bot_r # initiate next dirt target to bot coordinates
        self.dirt_c = bot_c 
        # Note If the bot is on a dirty cell, the cell will still have 'd' on it.

    # Find the nearest dirt (probably not the optimal route, always going to the nearest, but let's start with this)
    # Scan environment by looking at 'waves' around the current bot position
    def search_dirt(self):

        r, c = self.bot_r, self.bot_c

        # Check if the bot is currently on a dirty spot
        if self.grid[r][c] == self.dirt_marker:
            self.dirt_r = r
            self.dirt_c = c
            # print(f"Bot is on dirt location: {r}, {c}")
            return
        
        # Else, if de marker of the bot location is not a 'd' but it has the same coordinates, 
        # this means the grid was just initialized or the place was just cleaned and we need a new search.
        elif self.bot_r == self.dirt_r and self.bot_c == self.dirt_c:
            wave = 0 # initiate variable
            for i in range(5):
                wave += 1
                # print('--------------------'+str(wave))

                # Get all the cells in the outer 'shell' or 'wave' **
                top_row = [[-wave, col] for col in range(-wave, wave+1)]
                bottom_row = [[wave, col] for col in range(-wave, wave+1)]
                left_row = [[row, -wave] for row in range(-wave+1, wave)]
                right_row = [[row, wave] for row in range(-wave+1, wave)]

                directions = top_row + bottom_row + left_row + right_row

                # # ** Uncomment this to see the above working
                # zeros = np.zeros((2*wave+1, 2*wave+1))
                # print(zeros)
                # for position in directions:
                #     zeros[wave + position[0]][wave + position[1]] = 1
                # print(zeros)
                
                for direction in directions:
                    r, c = self.bot_r + direction[0], self.bot_c + direction[1]
                    # print(f'--TRY r, c = {r}, {c}')

                    # Check if the index is out of bound
                    if r < 0 or r >= 5 or c < 0 or c >= 5:
                        continue

                    # Check if there's dirt 
                    if self.grid[r][c] == self.dirt_marker:
                        self.dirt_r = r
                        self.dirt_c = c
                        # print(f"Dirt found at {r}, {c}")
                        return
        
        elif self.bot_r != self.dirt_r or self.bot_c != self.dirt_c:
            # No need to do another search, the bot hasn't reached the dirt yet, just move on.
            return

        else:
            print(f"search_dirt()/Error at Bot coordinates ({self.bot_r}, {self.bot_c}) and Dirt coordinates ({self.dirt_r}, {self.dirt_c}).")

        # If nothing was found, do nothing
        # We'll know that if the dirt coordinates don't change, all dirt is cleaned
        self.dirt_r, self.dirt_c = None, None
        print('The end.')
        return

    # Determine and make the next step based on next dirt target
    def next_step(self):
        # Either the bot position equals the dirt
        if self.bot_r == self.dirt_r and self.bot_c == self.dirt_c:
            self.grid[self.bot_r][self.bot_c] = 'b'
            return 'CLEAN'

        # Either the dirt is one step away
        elif self.dirt_r - self.bot_r == -1 and self.dirt_c - self.bot_c == 0:
            self.grid[self.bot_r][self.bot_c] = '-'
            self.bot_r, self.bot_c = self.dirt_r, self.dirt_c
            return 'UP'
        elif self.dirt_r - self.bot_r == 0 and self.dirt_c - self.bot_c == 1:
            self.grid[self.bot_r][self.bot_c] = '-'
            self.bot_r, self.bot_c = self.dirt_r, self.dirt_c
            return 'RIGHT'
        elif self.dirt_r - self.bot_r == 1 and self.dirt_c - self.bot_c == 0:
            self.grid[self.bot_r][self.bot_c] = '-'
            self.bot_r, self.bot_c = self.dirt_r, self.dirt_c
            return 'DOWN'
        elif self.dirt_r - self.bot_r == 0 and self.dirt_c - self.bot_c == -1:
            self.grid[self.bot_r][self.bot_c] = '-'
            self.bot_r, self.bot_c = self.dirt_r, self.dirt_c
            return 'LEFT'

        # Either the  dirt is > 1 step away
        elif self.dirt_r - self.bot_r < 0:
            self.grid[self.bot_r][self.bot_c] = '-'
            self.bot_r = self.bot_r - 1
            self.grid[self.bot_r][self.bot_c] = 'b'
            return 'UP'
        elif self.dirt_r - self.bot_r > 0:
            self.grid[self.bot_r][self.bot_c] = '-'
            self.bot_r = self.bot_r + 1
            self.grid[self.bot_r][self.bot_c] = 'b'
            return 'DOWN'
        elif self.dirt_c - self.bot_c < 0:
            self.grid[self.bot_r][self.bot_c] = '-'
            self.bot_c = self.bot_c - 1
            self.grid[self.bot_r][self.bot_c] = 'b'
            return 'LEFT'
        elif self.dirt_c - self.bot_c > 0:
            self.grid[self.bot_r][self.bot_c] = '-'
            self.bot_c = self.bot_c + 1
            self.grid[self.bot_r][self.bot_c] = 'b'
            return 'RIGHT'
        
        # ..or there is an error
        else:
            return f"next_step()/Error at Bot coordinates ({self.bot_r}, {self.bot_c}) and Dirt coordinates ({self.dirt_r}, {self.dirt_c})."

    # Execute steps
    def clean(self):
        self.search_dirt()
        next_step = self.next_step()
        print(next_step)



# Collect the input
posr, posc = list(map(int, input().split()))
board = []
for i in range(5):
    new_line = input().strip()
    row_to_add = [char for char in new_line]
    board.append(row_to_add)

print("THE GRID")
print(board)

if __name__ == '__main__':
    grid = Grid(board, posr, posc)
    for _ in range(25):
        next_move(posr, posc, board)