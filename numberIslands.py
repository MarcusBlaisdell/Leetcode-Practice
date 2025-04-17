'''
Leetcode 200
Number of Islands

Given an m x n 2D binary grid grid which represents a map of
'1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all
four edges of the grid are all surrounded by water.

If space to the left and to the top is 1, connected,
else, not connected, increment count
E.G.
11110
11010
11000
00000

[0][0],
- left is off grid, 0, not connected
- top is off grid, 0, not connected
- increment count
[0][1]
- left is 1, connected, move on
[0][2]
- left is 1, connected, move on
[0][3]
- left is 1, connected, move on
[1][0]
- left is off grid, 0, not connected
- top is 1, connected, move on
[1][1]
- left is 1, connected, move on
[1][2] is 0, move on
[1][3]
- left is 0, not connected
- top is 1, connected, move on
[1][4] is 0, move on
[2][0]
- left is off grid, 0, not connected
- top is 1, connected
[2][1]
- left is 1, connected, move on
[2][2] is 0, move on
[2][3] is 0, move on
[2][4] is 0, move on
11110
11010
11000
00000
[3][0] is 0, move on
[3][1] is 0, move on
[3][2] is 0, move on
[3][3] is 0, move on
[3][4] is 0, move on
return count
'''
from typing import List

def numIslands(grid: List) -> int:
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if c - 1 < 0:
                left = "0"
            else:
                left = grid[r][c-1]
            if r - 1 < 0:
                top = "0"
            else:
                top = grid[r-1][c]
            if (left == "0") and (top == "0") and (grid[r][c] == "1"):
                count += 1

    return count

def main() -> None:
    '''
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]

    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","0","1","1"],
            ["0","0","0","1","1"]]
    '''

    input = [[[["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]],1],
            [[["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","0","1","1"],
            ["0","0","0","1","1"]],2],
            [[["1","1","1"],
            ["0","1","0"],
            ["1","1","1"]],1]]

    for x in input:
        solution = numIslands(x[0])
        print("Solution s/b: ", x[1], " is: ", solution)

if __name__=='__main__':
    main()
