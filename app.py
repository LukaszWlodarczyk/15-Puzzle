import argparse
import random
import time

# GLOBAL VARIABLES
SOLVED_BOARD_2x2 = [[1, 2], [3, 0]]
SOLVED_BOARD_3x3 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
SOLVED_BOARD_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
START_BOARD = []
EMPTY_FIELD = {}
ORDER = []
DEPTH = 25


class Node:
    def __init__(self, current_board, parent, last_move, way):
        self.board = current_board
        # children['L'] - dziecko po ruchu w lewo, R prawo itd jakby cos XD
        self.children = {}
        # sekwencja ruch : błąd jaki po tym ruchu bedzie
        self.errors = {}
        if parent != 'Root':
            self.parent = parent
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


def remove_ways_to_out_of_board(current_node, flag=False):
    if EMPTY_FIELD['column'] == 2 and EMPTY_FIELD['row'] == 2:
        current_node.to_visit.remove('R')
        current_node.to_visit.remove('D')
    elif EMPTY_FIELD['column'] == 2 and EMPTY_FIELD['row'] == 0:
        current_node.to_visit.remove('R')
        current_node.to_visit.remove('U')
    elif EMPTY_FIELD['column'] == 0 and EMPTY_FIELD['row'] == 0:
        current_node.to_visit.remove('L')
        current_node.to_visit.remove('U')
    elif EMPTY_FIELD['column'] == 0 and EMPTY_FIELD['row'] == 2:
        current_node.to_visit.remove('L')
        current_node.to_visit.remove('D')
    elif EMPTY_FIELD['column'] == 0:
        current_node.to_visit.remove('L')
    elif EMPTY_FIELD['column'] == 2:
        current_node.to_visit.remove('R')
    elif EMPTY_FIELD['row'] == 0:
        current_node.to_visit.remove('U')
    elif EMPTY_FIELD['row'] == 2:
        current_node.to_visit.remove('D')
    if not flag:
        if current_node.last == 'R':
            current_node.to_visit.remove('L')
        elif current_node.last == 'L':
            current_node.to_visit.remove('R')
        elif current_node.last == 'U':
            current_node.to_visit.remove('D')
        elif current_node.last == 'D':
            current_node.to_visit.remove('U')


def is_solved (board):
    if board == SOLVED_BOARD_3x3:
        return True


def find_and_set_empty_field(board):
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[j][i] == '0':
                EMPTY_FIELD['row'] = j
                EMPTY_FIELD['column'] = i


# Algorithms
def dfs():
    current_node = Node(START_BOARD, 'Root', None, [])
    root_flag = True
    remove_ways_to_out_of_board(current_node, root_flag)
    while True:
        if is_solved(current_node.board):
            return "Rozwiazano"
        elif len(current_node.way) == DEPTH:
            #print('Switched')
            current_node = current_node.parent
            find_and_set_empty_field(current_node.board)
        elif len(current_node.to_visit) != 0:
            if not root_flag:
                try:
                    remove_ways_to_out_of_board(current_node, root_flag)
                except ValueError:
                    # Wystepuje gdy chcemy usunac ruch ktorego nei ma w tablicy
                    # print(ValueError)
                    pass
            if len(current_node.to_visit) != 0:
                move = current_node.to_visit[0]
                current_node.make_move(move)
                current_node.to_visit.remove(move)
                current_node = current_node.children[move]
                find_and_set_empty_field(current_node.board)
                root_flag = False
            else:
                if current_node.last is None:
                    return ("Nie znaleziono rozwiazania")
                else:
                    current_node = current_node.parent
                    find_and_set_empty_field(current_node.board)
        else:
            if current_node.last is None:
                return("Nie znaleziono rozwiazania")
            else:
                current_node = current_node.parent
                find_and_set_empty_field(current_node.board)


def bfs():
    current_node = Node(START_BOARD, 'Root', None, [])
    remove_ways_to_out_of_board(current_node, True)
    queue = []
    while True:
        if is_solved(current_node.board):
            return "Rozwiazano"
        else:
            try:
                remove_ways_to_out_of_board(current_node, False)
            except ValueError:
                # Wystepuje gdy chcemy usunac ruch ktorego nei ma w tablicy
                print(ValueError)
            for move in current_node.to_visit:
                current_node.make_move(move)
                current_node = current_node.children[move]
                queue.append(current_node)
                last_move = current_node.way[-1]
                change_position_of_blank_field(last_move)
                current_node = current_node.parent
            try:
                if current_node.last is not None:
                    queue.remove(current_node)
            except ValueError:
                print(current_node.way)
            current_node = queue[0]
            find_and_set_empty_field(current_node.board)


def astr(heuristic):
    def get_index_of_value(board, value):
        for index_row, row in enumerate(board):
            for index_col, elem in enumerate(row):
                if elem == value:
                    return index_row, index_col
    if heuristic == 'manh':
        def calculate_error(current_board, solved_board):
            error = 0
            for index_row, row in enumerate(current_board):
                for index_col, elem in enumerate(row):
                    target_row, target_col = get_index_of_value(solved_board, elem)
                    error += abs(index_row - target_row) + abs(index_col - target_col)
            return error
    else:
        def calculate_error(current_board, solved_board):
            error = 0
            for index_row, row in enumerate(current_board):
                for index_col, elem in enumerate(row):
                    target_row, target_col = get_index_of_value(solved_board, elem)
                    if abs(index_row - target_row) + abs(index_col - target_col) != 0:
                        error += 1
            return error
    current_node = Node(START_BOARD, 'Root', None, [])
    remove_ways_to_out_of_board(current_node, True)
    while True:

        if is_solved(current_node.board):
            return 'Rozwiazano'
        else:
            for move in current_node.to_visit:
                current_node.make_move(move)
                current_node = current_node.children[move]
                error = calculate_error(current_node.board, SOLVED_BOARD_3x3)
                current_node = current_node.parent
                find_and_set_empty_field(current_node.board)
                current_node.errors[move] = error
            min_value = min(current_node.errors.values())
            for key in current_node.errors:
                if current_node.errors[key] == min_value:
                    next_move = key
            current_node.make_move(next_move)
            current_node = current_node.children[next_move]
            try:
                remove_ways_to_out_of_board(current_node, False)
            except ValueError:
                print(ValueError)


if __name__ == '__main__':
    start_time = time.time()
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
    find_and_set_empty_field(START_BOARD)
    print(astr('hamm'))
    #print(bfs())
    #print("--- %s seconds ---" % (time.time() - start_time))


