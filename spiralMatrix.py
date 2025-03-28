'''
Spiral Matrix
LeetCode 54
2025-03-28
'''


def spiralOrder(matrix):
    result = []
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while (top < bottom) and (left < right):
        # get every i in the top row
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # get every i in the right column
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        '''
        Using initial test data, the while condition
        becomes false here, but doesn't break the while loop
        until after it completes a full iteration
        Adding a check at this point is needed to catch this
        and break out of the loop
        '''

        if not((top < bottom) and (left < right)):
            break

        # get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        # get every i in left column
        for i in range(bottom - 1, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result

def main():
    '''
    test 1:
    1  2  3  4
    5  6  7  8
    9 10 11 12
    Expected answer:
    1 2 3 4 8 12 11 10 9 5 6 7
    My answer:
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    '''
    #matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    '''
    test 2:
     1  2  3
     4  5  6
     7  8  9
    10 11 12
    Expected answer:
    1 2 3 6 9 12 11 10 7 4 5 8
    My answer:
    [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    '''
    matrix = [[1,2,3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    result = spiralOrder(matrix)
    print("result: ", result)

if __name__=='__main__':
    main()
