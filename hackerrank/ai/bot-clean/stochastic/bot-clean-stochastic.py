'''
Second version of BotClean assigment, this time in stochastic world.
'''

def nextMove(posr, posc, board):

    # Find the dirt
    for i in range(5):
        if 'd' in board[i]:
            dirt_i = board[i].index('d')
            r, c = i, dirt_i
    
    # Go to the dirt
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
    
