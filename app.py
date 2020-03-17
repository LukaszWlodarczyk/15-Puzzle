import argparse

# GLOBAL VARIABLES
SOLVED_BOARD_2x2 = [[1, 2], [3, 0]]
SOLVED_BOARD_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
SOLVED_BOARD_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
START_BOARD = []

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

