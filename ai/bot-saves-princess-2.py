#

def nextMove(n,r,c,grid):
    g = Grid(n, r, c, grid)

    return g.next_move()

class Grid(object):

    def __init__(self, n, r, c, grid):
        self.n = n
        self.bot_coordinates = (r, c)
        self.matrix = grid
        self.errors = []
        self.princess_marker = 'p'

    def has_valid_row_count(self):
        return self.n == len(self.matrix)

    def has_valid_column_count(self):
        for i in self.matrix:
            if not len(i) == self.n:
                self.errors.append('Grid expected column size %s but got %s' % (self.n, len(i)))
                return False
        return True
                
    def is_valid(self):
        r = True
        if not self.has_valid_row_count():
            self.errors.append('Grid expected row size %s but got %s' % (self.n, len(self.matrix)))
            r = False
        if not self.has_valid_column_count():
            r = False
        return r
    
    def find_coordinates(self, marker):
        for i, row in enumerate(self.matrix):
            if marker in row:
                row_index = i
                column_index = row.index(marker)
                return [row_index, column_index]
    
    def next_move(self):
        princess_coordinates = self.find_coordinates('p')

        horizontal_distance = princess_coordinates[1] - self.bot_coordinates[1]
        vertical_distance = princess_coordinates[0] - self.bot_coordinates[0]

        path = ""

        if horizontal_distance == 0:
            pass
        elif horizontal_distance < 0:
            return 'LEFT'
        else:
            return 'RIGHT'
        
        if vertical_distance == 0:
            pass
        elif vertical_distance < 0:
            return "UP"
        else:
            return 'DOWN'


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))


