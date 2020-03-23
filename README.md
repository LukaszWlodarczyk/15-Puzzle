# Fifteen Puzzle Solver
Python 3.8

To start use in command line:\
    **python app.py [dfs | bfs | astr] [(ORDER) | (heuristic)] path_to_file_with_board.txt path_to_file_with_solution path_to_file_with_statistic.txt**\
    !!! If you use dfs or bfs, use ORDER (R - move right, L - move left, D- move down, U - move up) **JUST CAPITAL LETTERS**, \
    !!! else use heuristic (manh - Manhattan, hamm - Hamming)\
    examples:\
      **python app.py dfs RLUD start_board.txt solution_board.txt stats_board.txt\
      python app.py astr hamm start_board.txt solution_board.txt stats_board.txt**

Default values:
  - max depth in dfs = 20
  - board size = 4 x 4
  - solved board has numbers in ascending order starting from 1

File with start board format: \
  number_of_rows number_of_columns\
  nr1 nr2 nr3 ...\
  .\
  .\
  .\
  Example:\
  4 4\
  1 2 3 4\
  5 6 7 8\
  9 10 11 12\
  13 0 14 15

Order in statistic file:
1. Solution length
2. Visited nodes
3. Processed nodes 
4. Depth level
5. Execution time in ms
