'''
Leetcode 36
Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells
need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the
         digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not
    necessarily solvable.
    Only the filled cells need to be validated according to the
    mentioned rules.



Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top
left corner being modified to 8. Since there are two 8's in
the top left 3x3 sub-box, it is invalid.



Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

Runtime beats 65.01%
Memory beats 86.06%
'''

def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r = True

        # Check rows:
        for i in range(9):
            a = []
            for j in range(9):
                if board[i][j] != ".":
                    b = int(board[i][j])
                    if b in a:
                        return False
                    else:
                        a.append(b)

        # Check columns:
        for i in range(9):
            a = []
            for j in range(9):
                if board[j][i] != ".":
                    b = int(board[j][i])
                    if b in a:
                        return False
                    else:
                        a.append(b)

        # Check 3x3 sub blocks:
        for x in range(3):
            for y in range(3):
                # check 3x3:
                a = []
                for i in range(3):
                    for j in range(3):
                        if board[i+(3*x)][j+3*y] != ".":
                            b = int(board[i+(3*x)][j+3*y])
                            if b in a:
                                return False
                            else:
                                a.append(b)

        return r

def main() -> None:
    test = [([["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], True),
            ([["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], False),
            ([[".",".",".",".","5",".",".","1","."]
            ,[".","4",".","3",".",".",".",".","."]
            ,[".",".",".",".",".","3",".",".","1"]
            ,["8",".",".",".",".",".",".","2","."]
            ,[".",".","2",".","7",".",".",".","."]
            ,[".","1","5",".",".",".",".",".","."]
            ,[".",".",".",".",".","2",".",".","."]
            ,[".","2",".","9",".",".",".",".","."]
            ,[".",".","4",".",".",".",".",".","."]], False)]

    for i in test:
        a = isValidSudoku(i[0])
        print("s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
