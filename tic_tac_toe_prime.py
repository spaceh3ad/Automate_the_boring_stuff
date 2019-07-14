#completed example from the book

import sys
import os
import itertools
import collections

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

winning_arrays = (('top-L','top-M','top-R'),('mid-L','mid-M','mid-R'),('low-L','low-M','low-R'),
                  ('top-L','mid-L','low-L'),('top-M','mid-M','low-M'),('top-R','mid-R','low-R'),
                  ('top-L','mid-M','low-R'),('top-R','mid-M','low-L'))

winning_arrayX = []
winning_arrayO = []

def check_win_X(board1, winning_arrays):

    global winning_arrayX
    # print(winning_arrayX)

    if tura == 4:
        # print(winning_arrayX)
        for k in range(len(winning_arrays)):
            if(collections.Counter(winning_arrayX) == collections.Counter(winning_arrays[k])) == True:
                print('Xs winning: ',winning_arrayX)
                print('X has won!')
                sys.exit()

    if tura > 4 and tura <= 8:
        winning_arrayX_temp = list(itertools.combinations((winning_arrayX),3))
        # print(winning_arrayX_temp)

        for i in range(len(winning_arrayX_temp)):
            for k in range(len(winning_arrays)):
                if(collections.Counter(winning_arrayX_temp[i]) == collections.Counter(winning_arrays[k])) == True:
                    print('Xs winning :',winning_arrayX_temp[i])
                    print('X has won!')
                    # print(winning_arrays)
                    sys.exit()


def check_win_O(board2, winning_arrays):

    global winning_arrayO

    if tura == 5:
        # print(winning_arrayO)
        for k in range(len(winning_arrays)):
            if(collections.Counter(winning_arrayO) == collections.Counter(winning_arrays[k])) == True:
                print('Os winning: ',winning_arrayO)
                print('O has won!')
                sys.exit()

    if tura > 5 and tura <= 8:
        winning_arrayO_temp = list(itertools.combinations((winning_arrayO),3))
        # print(winning_arrayO_temp)

        for i in range(len(winning_arrayO_temp)):
            for k in range(len(winning_arrays)):
                if(collections.Counter(winning_arrayO_temp[i]) == collections.Counter(winning_arrays[k])) == True:
                    print('Os winning: ',winning_arrayO_temp[i])
                    print('O has won!')
                    sys.exit()



tura = 0
while tura<9:
    try:
        turn = 'X'
        print('Moves: ',theBoard.keys())
        printBoard(theBoard)
        for tura in range(9):
            print('Turn for ' + turn + '. Move on which space?\n')
            move = input()
            os.system('clear')
            if(theBoard[move] != ' '):
                print('Already taken...')
                printBoard(theBoard)
                print('\n')
                continue
            else:
                theBoard[move] = turn
                printBoard(theBoard)
            if turn == 'X':
                winning_arrayX.append(move)
                check_win_X(theBoard, winning_arrays)
                turn = 'O'
            else:
                winning_arrayO.append(move)
                check_win_O(theBoard, winning_arrays)
                turn = 'X'
    except KeyError:
        print('Wrong input, no such field!\n')
    except KeyboardInterrupt:
        print('Quitting...')
        sys.exit()
