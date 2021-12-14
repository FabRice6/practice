'''
Solved with maximum score.

Principle: Take the grid input each time, find closest dirt and take one step.
'''

def next_move(posr, posc, board):
    # Find all the dirt
    dirts = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                dirts.append([i,j])
    
    print(f'List of dirt: {dirts}')

    # Find nearest dirt
    distances = []
    for dirt in dirts:
        total_steps = abs(dirt[0] - posr) + abs(dirt[1] - posc)
        distances.append(total_steps)
    
    print(f"List of distances: {distances}")

    min_distance_index = distances.index(min(distances))
    next_dirt = dirts[min_distance_index]
    r, c = next_dirt

    print(f'Next dirt: {r}, {c}')

    if r == posr and c == posc:
        print("CLEAN")
    elif r < posr:
        print("UP")
    elif r > posr:
        print('DOWN')
    elif c < posc:
        print('LEFT')
    elif c > posc:
        print('RIGHT')
    else:
        print('Error')

if __name__ == '__main__':
    # Collect the input
    posr, posc = list(map(int, input().split()))
    board = []
    for i in range(5):
        new_line = input().strip()
        row_to_add = [char for char in new_line]
        board.append(row_to_add)

    next_move(posr, posc, board)