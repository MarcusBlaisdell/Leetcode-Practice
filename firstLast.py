'''
Leetcode 34
Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]



Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non-decreasing array.
    -10^9 <= target <= 10^9


'''
import time
from typing import List

def searchRange(nums: List, target: int) -> List:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

def main() -> None:
    t1 = time.time()

    input = [([5,7,7,8,8,10], 8, [3,4]),
            ([5,7,7,8,8,10], 6, [-1,-1]),
            ([], 0, [-1,-1])]

    for i in input:
        a = searchRange(i[0], i[1])
        print("s/b: ", i[2], ", is: ", a)

    print("total time: ", time.time() - t1)

if __name__=='__main__':
    main()
