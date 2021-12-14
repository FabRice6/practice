"""
Pacman with DFS - without numpy

WARNING: Solution is not optimal

In order to maintain uniformity across submissions, please follow the below mentioned order in pushing nodes to stack. If a node has all the 4 adjacent neighbors. Then,

UP is inserted first into the stack, 
followed by LEFT, 
followed by RIGHT 
and then by DOWN.

Test input:
3 9  
5 1  
7 20  
%%%%%%%%%%%%%%%%%%%%
%--------------%---%  
%-%%-%%-%%-%%-%%-%-%  
%--------P-------%-%  
%%%%%%%%%%%%%%%%%%-%  
%.-----------------%  
%%%%%%%%%%%%%%%%%%%%  
"""

def dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    pacman = [pacman_r, pacman_c]
    grid = Grid(pacman, grid)
    stack = grid.findFood()
    grid.printOutput(stack)

class Grid(object):

    def __init__(self, pacman, grid) -> None:
        super().__init__()
        self.pacman = pacman
        self.food_marker = '.'
        self.wall_marker = chr(37)
        self.hall_marker = '-'
        self.visited_marker = '='
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
    
    def nextStep(self, pr, pc):
        next_steps = ['UP', 'LEFT', 'RIGHT', 'DOWN']
        next_positions = [
            [pr - 1, pc],
            [pr, pc - 1],
            [pr, pc + 1],
            [pr + 1, pc]
        ]
        # print(f"Next positions: {next_positions}")

        for i, position in enumerate(next_positions):
            r, c = position

            # Check for out of bound indexes
            if r < 0 or c < 0 or r >= self.rows or c >= self.columns:
                continue
            # If the next position is visited
            elif self.grid[r][c] == self.visited_marker:
                # print('Already visited')
                continue
            elif self.grid[r][c] == self.food_marker:
                # print('Food found')
                return 'FOOD!', position
            # If the next position is a wall
            elif self.grid[r][c] == self.wall_marker:
                # print('Hit a wall')
                continue
            elif self.grid[r][c] == self.hall_marker:
                # print('Found a next step !!')
                self.grid[r][c] = '='
                return next_steps[i], position
        
        self.grid[r][c] = '='
        return 'Blocked', [0,0]
    
    
    def findFood(self):
        pr, pc = self.pacman
        # path = [] # names of movements
        stack = [[pr, pc]] # coordinates of the path
        # for i in range(20):
        while 0 == 0:
            next_step, next_position = self.nextStep(pr, pc)
            # print(f'ITERATION: [{pr}, {pc}]')
            # if pr == 3 and pc == 8:
            #     break
            if next_step == 'FOOD!':
                stack.append(next_position)
                # print(stack)
                return stack
            elif next_step == 'Blocked':
                # print(stack)
                stack.pop()
                # print(stack)
                pr, pc = stack[-1]
            else:
                stack.append(next_position)
                pr, pc = next_position

    def printOutput(self, stack):
        output = str(len(stack) - 1)
        for position in stack:
            output += '\n' + ' '.join(map(str,position))
        
        print(output)
    

# Collect the input
pacman_r, pacman_c = list(map(int, input().split()))
food_r, food_c = list(map(int, input().split()))
r, c = list(map(int, input().split()))
grid = []
for i in range(r):
    new_line = input().strip()
    row_to_add = [char for char in new_line]
    grid.append(row_to_add)

# print("THE GRID")
# print(grid)

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)