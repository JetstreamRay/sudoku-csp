import sys
import copy

class varNode:
    def __init__(self, value, domain=[1,2,3,4,5,6,7,8,9]):
        self.value = value
        if value != 0:
            self.domain = domain 
        else:
            self.domain = [value]
       
class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints


class Sudoku(object):
    def __init__(self, puzzle):
        # you may add more attributes if you need
        self.puzzle = puzzle # self.puzzle is a list of lists
        self.ans = copy.deepcopy(puzzle) # self.ans is a list of lists
        # self.state = [[varNode(value) for value in row] for row in puzzle]

    @staticmethod
    def makeRowConsistent(self, node, row):
        for i in row:
            if i.value in node.domain:
                node.domain.remove(i.value)

    def solve(self):
        #TODO: Your code here
        def boxRange(x): return range((x/3)*3,(x/3)*3+3)
        def arcgen(x,y):
            return ['v'+str(i)+str(j) for i in range(0,9) for j in range(0,9) if 
                (i != x or y != j) and (i == x or j == y or (i in boxRange(x) and j in boxRange(y)))]
        variables = [('v'+str(i)+str(j), v) for i, row in enumerate(self.puzzle) for j, v in enumerate(row[0:-1])]
        domains = {key: (range(1,10) if v == '0' else [int(v)]) for (key, v) in variables}
        arcs = {key: arcgen(int(key[1]),int(key[2])) for (key, v) in variables}
        # don't print anything here. just return the answer
        # self.ans is a list of lists
        return self.ans

    # you may add more classes/functions if you think is useful
    # However, ensure all the classes/functions are in this file ONLY

if __name__ == "__main__":
    # STRICTLY do NOT modify the code in the main function here
    if len(sys.argv) != 3:
        print ("\nUsage: python sudoku_A2_xx.py input.txt output.txt\n")
        raise ValueError("Wrong number of arguments!")

    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        print ("\nUsage: python sudoku_A2_xx.py input.txt output.txt\n")
        raise IOError("Input file not found!")

    puzzle = [[0 for i in range(9)] for j in range(9)]
    lines = f.readlines()

    i, j = 0, 0
    for line in lines:
        for number in line:
            if '0' <= number <= '9':
                puzzle[i][j] = int(number)
                j += 1
                if j == 9:
                    i += 1
                    j = 0

    sudoku = Sudoku(puzzle)
    ans = sudoku.solve()

    with open(sys.argv[2], 'a') as f:
        for i in range(9):
            for j in range(9):
                f.write(str(ans[i][j]) + " ")
            f.write("\n")
