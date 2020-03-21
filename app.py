import argparse
import random

# GLOBAL VARIABLES
SOLVED_BOARD_2x2 = [[1, 2], [3, 0]]
SOLVED_BOARD_3x3 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
SOLVED_BOARD_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
START_BOARD = []
EMPTY_FIELD = {}
ORDER = []


class Node:
    def __init__(self, current_board, parent, last_move, way):
        self.board = current_board
        # children['L'] - dziecko po ruchu w lewo, R prawo itd jakby cos XD
        self.children = {}
        if parent != 'Root':
            self.parent = parent
            # To nizej potrzebne do tego zeby nie sprawdzal mozliwosci cofania sie czyli jak ostatni byl w dol
            # to zeby nie szedl do gory
            self.last = last_move
        # A to jest jakie ruchy do tego doprowadzily
        self.way = way.copy()
        self.way.append(last_move)
        # Kolejka do odwiedzenia, na razie uzyta w dfsie
        self.to_visit = ORDER.copy()

    def create_child(self, board_after_move, move):
        child = Node(board_after_move, self, move, self.way)
        self.children[move] = child

    def make_move(self, move):
        y = EMPTY_FIELD['row']
        x = EMPTY_FIELD['column']
        if move == 'L':
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y][x - 1], tmp_array[y][x] = tmp_array[y][x], tmp_array[y][x - 1]
            EMPTY_FIELD['column'] -= 1
            self.create_child(tmp_array, move)
        elif move == 'R':
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y][x], tmp_array[y][x + 1] = tmp_array[y][x + 1], tmp_array[y][x]
            EMPTY_FIELD['column'] += 1
            self.create_child(tmp_array, move)
        elif move == 'U':
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y - 1][x], tmp_array[y][x] = tmp_array[y][x], tmp_array[y - 1][x]
            EMPTY_FIELD['row'] -= 1
            self.create_child(tmp_array, move)
        elif move == 'D':
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y][x], tmp_array[y + 1][x] = tmp_array[y + 1][x], tmp_array[y][x]
            EMPTY_FIELD['row'] += 1
            self.create_child(tmp_array, move)


# Auxiliary functions
def change_position_of_blank_field(last_move):
    if last_move == 'U':
        EMPTY_FIELD['row'] += 1
    if last_move == 'D':
        EMPTY_FIELD['row'] -= 1
    if last_move == 'L':
        EMPTY_FIELD['column'] += 1
    if last_move == 'R':
        EMPTY_FIELD['column'] -= 1


def remove_ways_to_out_of_board(current_node):
    if EMPTY_FIELD['column'] == 2:
        current_node.to_visit.remove('R')
    elif EMPTY_FIELD['column'] == 0:
        current_node.to_visit.remove('L')
    elif EMPTY_FIELD['row'] == 2:
        current_node.to_visit.remove('D')
    elif EMPTY_FIELD['row'] == 0:
        current_node.to_visit.remove('U')


# Algorithms
def dfs():
    current_node = Node(START_BOARD, 'Root', None, [])
    root_flag = True
    remove_ways_to_out_of_board(current_node)
    while True:
        # TODO Randomowe printy do wyjebania
        print(current_node)
        print(current_node.board)
        print(current_node.way)
        if current_node.board == SOLVED_BOARD_3x3:
            return "Rozwiazano"
        elif len(current_node.way) == 20:
            print('Switched')
            last_move = current_node.way[-1]
            change_position_of_blank_field(last_move)
            current_node = current_node.parent
        elif len(current_node.to_visit) != 0:
            if not root_flag:
                try:
                    remove_ways_to_out_of_board(current_node)
                except ValueError:
                    # Wystepuje gdy chcemy usunac ruch ktorego nei ma w tablicy
                    print(ValueError)
            move = current_node.to_visit[0]
            current_node.make_move(move)
            current_node.to_visit.remove(move)
            current_node = current_node.children[move]
            root_flag = False
        else:
            current_node = current_node.parent


def bfs():
    pass


if __name__ == '__main__':

    # Parsing
    parser = argparse.ArgumentParser(description="Algorithm, order, source file, solution file, statistics file.")
    parser.add_argument('algorithm')
    parser.add_argument('order')
    parser.add_argument('source_file')
    parser.add_argument('solution_file')
    parser.add_argument('statistic_file')
    args = parser.parse_args()

    for elem in args.order:
        ORDER.append(elem)

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

    print(dfs())




