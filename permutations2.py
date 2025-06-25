'''
Leetcode 46
Permutations
Medium

Given an array nums of distinct integers, return all the possible
Permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]



Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

'''
import time
from typing import List

def permute(nums: List) -> List:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return nums

        r = []
        def helpPermute(hNums: List) -> int:
            r = []
            if len(hNums) > 1:
                b = hNums[:]
                b.remove(hNums[0])
                a = helpPermute(b)
            else:
                r.append(hNums[0])
            return r

        for i in range(len(nums)):
            b = nums[:]
            b.remove(nums[i])
            a = helpPermute(b)
            r.append(a)

        return r

def main() -> None:
    t1 = time.time()

    input = [([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
            ([0,1], [[0,1],[1,0]]),
            ([1], [[1]])
            ]

    for i in input:
        a = permute(i[0])
        print("s/b: ", i[1], ", is: ", a)

    print("total time: ", time.time() - t1 )

if __name__=='__main__':
    main()
