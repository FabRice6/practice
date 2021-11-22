'''
Tron game on HackerRank

(Din't spend much time on this one, it's pretty suboptimal)
'''

def next_move(board, player, player_r, player_c):
    if player == 'r':
        direction_names = [
            'UP',
            'DOWN',
            'RIGHT',
            'LEFT'
        ]
        directions = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1]
        ]
    else: 
        direction_names = [
            'UP',
            'DOWN',
            'LEFT',
            'RIGHT'
        ]
        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

    for i, dir in enumerate(directions):
        r, c = player_r + dir[0], player_c + dir[1]
        next_char = board[r][c]
        if next_char == '-':
            print(direction_names[i])
            return

if __name__ == '__main__':
    # Collect the input
    player = str(input())
    player_r, player_c, other_r, other_c = list(map(int, input().split()))
    board = []
    for i in range(15):
        new_line = input().strip()
        row_to_add = [char for char in new_line]
        board.append(row_to_add)

    next_move(board, player, player_r, player_c)
