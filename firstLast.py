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

88/88

Runtime beats 100%
Memory beats 30.21%
'''
import time
from typing import List

def searchRange(nums: List, target: int) -> List:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findLeft(s):
            '''
            conditions:
            lt < target, rt == target
                if (nums[lt] < target) and (nums[lt + 1] == target):
                    return lt
            lt == target, rt == target
                if (nums[lt] == target) and (nums[lt - 1] < target):
                    return lt - 1
            '''
            if nums[0] == target:
                return 0
            lt = 0
            rt = s

            while lt < rt:
                if (nums[lt] < target) and (nums[lt+1] == target):
                    return lt + 1
                if (nums[lt] == target and nums[lt - 1] < target):
                    return lt
                mid = (((rt - lt) // 2) + lt)
                if (nums[mid] < target):
                    lt = mid
                if (nums[mid] == target):
                    rt = mid

        def findRight(s):
            '''
            conditions:
            lt < target, rt == target
                if (nums[lt] < target) and (nums[lt + 1] == target):
                    return lt
            lt == target, rt == target
                if (nums[lt] == target) and (nums[lt - 1] < target):
                    return lt - 1
            '''
            if nums[len(nums) - 1] == target:
                return (len(nums) - 1)
            lt = s
            rt = len(nums) - 1

            while lt < rt:
                if (nums[rt] > target) and (nums[rt - 1] == target):
                    return rt - 1
                if (nums[rt] == target and nums[rt + 1] > target):
                    return rt
                mid = (((rt - lt) // 2) + lt)
                if (nums[mid] > target):
                    rt = mid
                if (nums[mid] == target):
                    lt = mid


        if len(nums) == 0:
            return [-1,-1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        if len(nums) == 2:
            lt = rt = -1
            if target in nums:
                if nums[0] == target:
                    lt = 0
                else:
                    lt = 1
                if nums[1] == target:
                    rt = 1
                else:
                    rt = 0
            return [lt, rt]

        # two binary searches
        # Find first instance:
        lt = 0
        rt = len(nums) - 1

        if nums[rt] == target:
            lt = findLeft(rt)
            rt = findRight(rt)
            return [lt, rt]
        # This will work for list sizes > 2:
        update = 1
        #while lt < (rt - 1):
        while update == 1:
            update = 0
            s = (((rt - lt) // 2) + lt)
            print("lt: ", lt, ", rt: ", rt, ", s: ", s)
            if nums[s] == target:
                lt = findLeft(s)
                rt = findRight(s)
                return [lt, rt]
            if nums[s] < target:
                if (((rt - lt) // 2) + lt) != lt:
                    lt = ((rt - lt) // 2) + lt
                    update = 1
            if nums[s] > target:
                if (((rt - lt) // 2) + lt) != rt:
                    rt = ((rt - lt) // 2) + lt
                    update = 1

        return [-1,-1]

def main() -> None:
    t1 = time.time()

    input = [([5,7,7,8,8,10], 8, [3,4]),
            ([5,7,7,8,8,10], 6, [-1,-1]),
            ([], 0, [-1,-1]),
            ([1], 0, [-1,-1]),
            ([1], 1, [0,0]),
            ([2,2], 0, [-1,-1]),
            ([2,2], 2, [0, 1]),
            ([1,3], 1, [0, 0]),
            ([1,2,3], 1, [0, 0]),
            ([1,2,3], 3, [2, 2])]

    for i in input:
        a = searchRange(i[0], i[1])
        print("s/b: ", i[2], ", is: ", a)

    print("total time: ", time.time() - t1)

if __name__=='__main__':
    main()
