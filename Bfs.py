import numpy as np
import queue
solved_board = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

board = np.array([[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 11, 15]])

print(board)


def isBoardSolved(current_board):
    if (current_board == solved_board).all():
        return True
    else: 
        return False


print(isBoardSolved(board))
queue = queue.Queue()
