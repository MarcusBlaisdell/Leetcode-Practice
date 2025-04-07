'''
Leetcode 152
Max Product Subarray
April 07, 2025
Given an integer array nums, find the contiguous
subarray within an array, containing at least
one number, which has the largest product
'''
from typing import List

def maxProduct(nums: List[int]) -> int:
    ans = 0
    curMin, curMax = 1, 1

    for n in nums:
        tmp = [n * curMax, n * curMin, n]
        curMax = max(tmp)
        curMin = min(tmp)
        ans = max(ans, curMax)

    return ans

def main() -> None:
    numsArray = [[2,3,-2,4],[-1,0],
                [-2,-1,0], [-2, -1, -3, 0],
                [-2, -1, -3, 0, 4],
                [-2, -1, -3, 0, 4, -5],
                [-2, -1, -3, 0, 4, -5, -1]]

    for nums in numsArray:
        ans = maxProduct(nums)
        print("answer: ", ans)

if __name__=='__main__':
    main()
