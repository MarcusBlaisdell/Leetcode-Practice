'''
Leetcode 48
Rotate Image
Medium


You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to
modify the input 2D matrix directly. DO NOT allocate another 2D
matrix and do the rotation.



Example 1:

From:
1,2,3
4,5,6
7,8,9
To:
7,4,1
8,5,2
9,6,3

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

From:
5,1,9,11
2,4,8,10
13,3,6,7
15,14,12,16
To:
15,13,2,5
14,3,4,1
12,6,8,9
16,7,10,11

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]



Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

21/21 test cases
Runtime beats 100%
Memory beats 86.89%
'''
import time
from typing import List

def rotate(matrix: List[List[int]]) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix
         in-place instead.
        """
        '''
        top row:
        (F, F:F, L), (F, F + 1:F, L - 1), ...
        right column:
        (F, L:F, F), (F + 1, L:F, F + 1), ...
        bottom row:
        (L, L:F, L), (L, L - 1: F + 1, L), ...
        left column:
        (L, F:L, L), (L - 1, F:L, L - 1), ...
        '''

        '''
        store val/each pos
        replace val/each pos
        '''
        fo = 0 # initial first outer/inner position
        lo = len(matrix[0]) - 1 # initial last outer/inner position

        while fo < lo:
            fi = fo
            li = lo
            while fi < lo:
                '''
                top = matrix[fo][fi]
                right = matrix[fi][lo]
                bottom = matrix[lo][li]
                left = matrix[li][fo]
                '''
                tmp = matrix[fo][fi] # tmp = top
                matrix[fo][fi] = matrix[li][fo] # top = left
                matrix[li][fo] = matrix[lo][li] # left = bottom
                matrix[lo][li] = matrix[fi][lo] # bottom = right
                matrix[fi][lo] = tmp # right = tmp
                fi += 1
                li -= 1
            fo += 1
            lo -= 1

def main() -> None:
    t1 = time.time()

    input = [([[1,2,3],[4,5,6],[7,8,9]],
            [[7,4,1],[8,5,2],[9,6,3]]),
            ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
            [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
            ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
            [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])]

    for i in input:
        rotate(i[0])
        print("s/b: ", i[1])
        print(", is: ", i[0])

    print("Total time: ", time.time() - t1)


if __name__=='__main__':
    main()
