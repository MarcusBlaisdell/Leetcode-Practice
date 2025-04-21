'''
Leetcode 200
Number of Islands

Given an m x n 2D binary grid grid which represents a map of
'1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all
four edges of the grid are all surrounded by water.

If space to the left and to the top is 1, connected,
else, not connected, increment count (Passes 33/49)
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
Fails on:
11111
00100
11111
--
method 2:
This is actually a graph, add connected nodes together,
count total nodes when complete
[0][0], list is empty, add to adjacency list
check right, down, if "1", add to adjacency list
11111
00100
11111

11000
11000
00000
00011
00011

11111
00100
11111
[0][0]: [0][1]
[0][1]: [0][0], [0][2]
[0][2]: [0][1], [0][3], [1][3]
[0][3]: [0][2], [0][4]
[0][4]: [0][3]
[1][0]:
[1][1]:
[1][2]: [0][2], [2][2]
[1][3]:
[1][4]:
[2][0]: [2][1]
[2][1]: [2][0]
[2][2]: [2][1], [1][2], [2][3]
[2][3]: [2][2], [2][4]
[2][4]: [2][3]

[0][0]: [0][1], can reach [0][1], set [0][1] to [0][0]
[0][1]: [0][0], can reach [0][2], set [0][2] to [0][0]
[0][2]: [0][0], can reach [0][3], set [0][3] to [0][0]
                can reach [1][2], set [1][2] to [0][0]
[0][3]: [0][0], can reach [0][4], set [0][3] to [0][0]
[0][4]: [0][0], no connections right, or down
[1][0]: 0
[1][1]: 0
[1][2]: [0][0], can reach [2][2], set [2][2] to [0][0]
[1][3]: 0
[1][4]: 0
[2][0]: can reach [2][1], set [2][1] to [2][0]
[2][1]:
[2][2]: [0][0]
[2][3]:
[2][4]:
Check left, down, right in recursive call?

[0][0]:
    - 1, root is empty, set to current position: [0][0]
    - nothing left, [0][-1]
    - down is 0, [1][0]
    - right is 1, [0][1], set [0][1] to current position root, [0][0]
        - recursive call on [0][1]
[0][1]:
[0][2]:
[0][3]:
[0][4]:
[1][0]:
[1][1]:
[1][2]:
[1][3]:
[1][4]:
[2][0]:
[2][1]:
[2][2]:
[2][3]:
[2][4]:
'''
from typing import List

'''
# This solution works for 33/49 test cases:
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
'''

def islandHelp(grid: List, root: List, node: tuple) -> None:
    r = len(grid)
    c = len(grid[0])
    print("r: ", r, ", c: ", c)
    # if current node already has a root,
    print("[",node[0],"][",node[1],"]")
    if root[node[0]][node[1]]:
        pass
    '''
    else:
        # set current nodes root to current node
        root[node[0]][node[1]] = [node[0]][node[1]]
    # check left, visit if exists and doesn't have a root:
    if node[1] - 1 > -1:
    #if grid[node[0]][node[1] - 1]:
        if (grid[node[0]][node[1] - 1] == "1") and (root[node[0]][node[1] - 1] == []):
            islandHelp(grid, root, (node[0],node[1] - 1)
    # check down, visit if exists and doesn't have a root:
    if (node[0] + 1) < r:
    #if grid[node[0] + 1][node[1]]:
        if (grid[node[0] + 1][node[1]] == "1") and (root[node[0] + 1][node[1]] == []):
            islandHelp(grid, root, (node[0] + 1,node[1]))
    # check right, visit if exists and doesn't have a root:
    if node[1] + 1 < c):
    #if grid[node[0]][node[1] + 1]:
        if (grid[node[0]][node[1] + 1] == "1") and (root[node[0]][node[1] + 1] == []):
            islandHelp(grid, root, (node[0],node[1] + 1))
    '''


def numIslands(grid: List) -> int:
    count = 0
    # use set instead of matrix
    root = [[[]] * len(grid)] * len(grid[0])

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if root[r][c] == []:
                islandHelp(grid, root, (r,c))

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
