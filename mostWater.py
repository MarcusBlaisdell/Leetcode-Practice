'''
Leetcode 11
Container With Most Water

You are given an integer array height of length n. There are n
vertical lines drawn such that the two endpoints of the ith line
are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:
   |              |
   |              |     |
   |  |           |     |
   |  |     |     |     |
   |  |     |  |  |     |
   |  |     |  |  |  |  |
   |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water
the container can contain is 49.
* I think it should be 55

Example 2:

Input: height = [1,1]
Output: 1



Constraints:

    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4

Runtime beats 88.27%
memory beats 85.83%
'''
from typing import List

def maxArea(height: List):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        l = 0
        r = len(height) - 1

        while l < r:
            if min(height[l], height[r]) * (r - l) > a:
                a = min(height[l], height[r]) * (r - l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        '''
        # Passes 55/65, exceeds time limit
        for i in range(l, r):
            j = r
            while j > i:
                if min(height[i], height[j]) * (j - i) > a:
                    a = min(height[i], height[j]) * (j - i)
                    r = j
                j -= 1
        '''

        '''
        while l < r:
            print("l: ", l, ", r: ", r)
            if min(height[l], height[r]) * (r - l) > a:
                a = min(height[l], height[r]) * (r - l)
            if l < len(height) - 2:
                if height[l+1] > height[l]:
                    l += 1
                else:
                    r -= 1
        '''

        '''
        # Passes 55/65, exceeds time limit
        for i in range(l, r):
            for j in range(r, -1, -1):
                if j < i:
                    break
                if min(height[i], height[j]) * (j - i) > a:
                    a = min(height[i], height[j]) * (j - i)
        '''

        return a

def main() -> None:
    test = [([1,8,6,2,5,4,8,3,7], 49),
            ([1,1], 1),
            ([2,3,4,5,18,17,6],17)]

    for i in test:
        a = maxArea(i[0])
        print("s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
