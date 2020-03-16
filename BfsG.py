import numpy as np

solved_board = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

def bfs_algorithm(root)
    explored, queue = set(), deque([State])