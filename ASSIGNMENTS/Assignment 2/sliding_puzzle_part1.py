# Felix Egan
# 2431927

import random as r
import time

def tileLabels(n): # works, verified
    tiles = []
    for num in range(1,n**2):
        tiles.append(str(num))
    tiles.append('  ')
    return tiles

def getNewPuzzle(n): # works, verified
    shuffled_tiles = tileLabels(n)
    r.shuffle(shuffled_tiles)
    puzzle = []
    for i in shuffled_tiles:
        if len(i)==1 and i!='  ':
            shuffled_tiles[shuffled_tiles.index(i)] = f'{i} '
    start_index = 0
    for _ in range(n):
        puzzle.append(shuffled_tiles[start_index:start_index+n])
        start_index += n
    return puzzle

def findEmptyTile(board): # works, verified
    row_index = 0
    colm_index = 0
    for row in board:
        for tile in row:
            if tile=='  ':
                row_index = board.index(row)
                colm_index = row.index(tile)
                break
    return (row_index, colm_index)

def displayBoard(board):
    n = len(board)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def nextMove(board):
    displayBoard(board)
    valid_moves = []
    empty_tile = findEmptyTile(board)

    if empty_tile[0] != 0: valid_moves.append('S')
    if empty_tile[0] != len(board)-1: valid_moves.append('W')
    if empty_tile[1] != 0: valid_moves.append('D')
    if empty_tile[1] != len(board)-1: valid_moves.append('A')

    print(f"                          ({'W' if 'W' in valid_moves else ' '})")
    print(f"Enter WASD (or QUIT): ({'A' if 'A' in valid_moves else ' '}) ({'S' if 'S' in valid_moves else ' '}) ({'D' if 'D' in valid_moves else ' '})")

    next_move = input('> ').upper()

    if next_move == 'QUIT':
        exit()
    
    if next_move not in valid_moves:
        print('Invalid move. Try again.')
        time.sleep(1) # Just so the user can read that the input is incorrect. Does involve importing time.
        nextMove(board)
    
n = int(input('Grid Size: '))
board = getNewPuzzle(n)
while True:
    nextMove(board)