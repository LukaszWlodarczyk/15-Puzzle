import argparse
import random

# GLOBAL VARIABLES
SOLVED_BOARD_2x2 = [[1, 2], [3, 0]]
SOLVED_BOARD_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
SOLVED_BOARD_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
START_BOARD = []
EMPTY_FIELD = {}


class Node:
    def __init__(self, current_board, parent, last_move, way):
        self.board = current_board
        self.children = {}
        if parent != 'Root':
            self.parent = parent
            self.last = last_move
        self.way = way.copy()
        self.way.append(last_move)

    def create_child(self, board_after_move, move):
        child = Node(board_after_move, self, move, self.way)
        self.children[move] = child

    def make_move(self, move):
        if move == 'L':
            if EMPTY_FIELD['column'] == 0:
                pass
            else:
                tmp_array = self.board.copy()
                tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column'] - 1], \
                tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column']] \
                    = tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column']], \
                      tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column'] - 1]
                EMPTY_FIELD['column'] -= 1
                self.create_child(tmp_array, move)
        elif move == 'R':
            if EMPTY_FIELD['column'] == len(START_BOARD[EMPTY_FIELD['row']]) - 1:
                pass
            else:
                tmp_array = self.board.copy()
                tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column']], \
                tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column'] + 1] \
                    = tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column'] + 1], \
                      tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column']]
                EMPTY_FIELD['column'] += 1
                self.create_child(tmp_array, move)
        elif move == 'U':
            if EMPTY_FIELD['row'] == 0:
                pass
            else:
                tmp_array = self.board.copy()
                tmp_array[EMPTY_FIELD['row'] - 1][EMPTY_FIELD['column']], \
                tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column']] \
                    = tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column']], \
                      tmp_array[EMPTY_FIELD['row'] - 1][EMPTY_FIELD['column']]
                EMPTY_FIELD['row'] -= 1
                self.create_child(tmp_array, move)
        elif move == 'D':
            if EMPTY_FIELD['row'] == len(START_BOARD[EMPTY_FIELD['column']]) - 1:
                pass
            else:
                tmp_array = self.board.copy()
                tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column']], \
                tmp_array[EMPTY_FIELD['row'] + 1][EMPTY_FIELD['column']] \
                    = tmp_array[EMPTY_FIELD['row'] + 1][EMPTY_FIELD['column']], \
                      tmp_array[EMPTY_FIELD['row']][EMPTY_FIELD['column']]
                EMPTY_FIELD['row'] += 1
                self.create_child(tmp_array, move)


if __name__ == '__main__':

    # Parsing
    parser = argparse.ArgumentParser(description="Algorithm, order, source file, solution file, statistics file.")
    parser.add_argument('algorithm')
    parser.add_argument('order')
    parser.add_argument('source_file')
    parser.add_argument('solution_file')
    parser.add_argument('statistic_file')
    args = parser.parse_args()

    # Loading start board from file
    with open(args.source_file) as board:
        first_line_flag = True
        for line in board:
            if first_line_flag:
                first_line_flag = False
                continue
            else:
                START_BOARD.append(line.split())

    # Setting coordinates of empty field
    for j in range(len(START_BOARD)):
        for i in range(len(START_BOARD[j])):
            if START_BOARD[j][i] == '0':
                EMPTY_FIELD['row'] = j
                EMPTY_FIELD['column'] = i

    root = Node(START_BOARD, 'Root', None, [])
    print(root.board)
    root.make_move('U')
    print(root.children['U'].board)
    print(root.children['U'].way)
    root.children['U'].make_move('L')
    print(root.children['U'].children['L'].board)
    print(root.children['U'].children['L'].way)
