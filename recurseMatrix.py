'''
Printing contents of a matrix recursively:
'''
from typing import List

def printMatrixHelp(grid: List, node: tuple) -> None:
    r = len(grid)
    c = len(grid[0])
    if node in visited:
        pass
    else:
        visited.add(node)
        if (node[1] - 1) > -1:
            printMatrixHelp(grid, (node[0], node[1] - 1))
            print(grid[node[0]][node[1]])
        if (node[0] + 1) < (r - 1):
            printMatrixHelp(grid, (node[0] + 1,node[1]))
            print(grid[node[0] + 1][node[1]])
        if (node[1] + 1) < (c - 1):
            printMatrixHelp(grid, (node[0], node[1] + 1))
            print(grid[node[0]][node[1] + 1])

def printMatrix(input: List[List[str]]):
    global visited
    visited = set()

    printMatrixHelp(input, (0,0))


def main() -> None:
    input = [["1","2","3","4","5"],
            ["6","7","8","9","10"],
            ["11","12","13","14","15"],
            ["16","17","18","19","20"]]

    printMatrix(input)

if __name__=='__main__':
    main()
