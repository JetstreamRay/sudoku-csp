# sudoku-csp
A Sudoku solver written as a constraint satisfaction problem. Used heuristics such as most constrained variable(aka MRV), least constraining value and AC3 to improve efficiency of the algorithm.

Example usage via command line as shown below, where input is a text of 9x9 integers. 0 represents empty space.

python sudoku_ac3.py input.txt output.txt

