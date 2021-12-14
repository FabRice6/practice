'''
Lights out on HackerRank

This solution got about 17 points.
'''

import random

def findCells(board):
    single_cells = []
    double_cells = []
    triple_cells = []
    all_cells = []

    for i in range(7):
        for j in range(7):
            if board[i][j] != 1: continue
            else:
                all_cells.append([i,j])
                down = False
                right = False
                if board[i+1][j] == 1: down = True
                if board[i][j+1] == 1: right = True

            if down == True and right == True:
                triple_cells.append([i,j])
            elif down == True or right == True:
                double_cells.append([i,j])
            if down == False and right == False:
                single_cells.append([i,j])
    
    return all_cells, triple_cells, double_cells, single_cells

def findNextMove(board):
    all, triples, doubles, singles = findCells(board)

    if len(all) != 0:
        next_move = random.choice(all)
    # if len(triples) != 0:
    #     next_move = random.choice(triples)
    # elif len(doubles) != 0:
    #     next_move = random.choice(doubles)
    # elif len(singles) != 0:
    #     next_move = random.choice(singles)
    else:
        next_move = [None, None]
    
    print(f"{next_move[0]} {next_move[1]}")


if __name__ == '__main__':
    # Collect the input
    player = int(input())
    board = []
    for i in range(8):
        new_line = input().strip()
        row_to_add = [int(char) for char in new_line]
        board.append(row_to_add)
    
    findNextMove(board)

    