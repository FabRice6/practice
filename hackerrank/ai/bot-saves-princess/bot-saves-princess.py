def displayPathtoPrincess(n,grid):
#print all the moves here
    g = Grid(n, grid)
    if not g.is_valid():
        raise Exception('Grid validation error: %s' % '\n'.join(g.errors))
    print(g.print_bot_path())



class Grid(object):

    def __init__(self, n, grid):
        self.n = n
        self.matrix = grid
        self.errors = []
        self.princess_marker = 'p'
        self.bot_marker = 'm'

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
    
    def print_bot_path(self):
        bot_coordinates = self.find_coordinates('m')
        princess_coordinates = self.find_coordinates('p')

        horizontal_distance = princess_coordinates[1] - bot_coordinates[1]
        vertical_distance = princess_coordinates[0] - bot_coordinates[0]

        path = ""

        if horizontal_distance == 0:
            pass
        elif horizontal_distance < 0:
            horizontal_direction = 'LEFT'
        else:
            horizontal_direction = 'RIGHT'
        
        if vertical_distance == 0:
            pass
        elif vertical_distance < 0:
            vertical_direction = "UP"
        else:
            vertical_direction = 'DOWN'
        
        for x in range(abs(horizontal_distance)):
            path += horizontal_direction + '\n'
        for x in range(abs(vertical_distance)):
            path += vertical_direction + '\n'

        return path

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)