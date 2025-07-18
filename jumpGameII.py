'''
Leetcode 45
Jump Game II
Medium

You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward
jump from index i. In other words, if you are at nums[i], you can
jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test
cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2



Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].


'''
from typing import List
import time

def jump(nums: List) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return 0
        i = 0
        j = 0

        while i <= len(nums):
            print("i: ", i)
            if i >= len(nums) - 1:
                return j + 1
            if i + nums[i] >= (len(nums) - 1):
                return j + 1
            else:
                for k in range(nums[i]):
                    m = 0
                    if (i + k + nums[i + k]) > m:
                        m = i + k + nums[i + k]
                        n = i + k
                if n == i:
                    return j + 1
                else:
                    i = n
            j += 1

        return j

def main() -> None:
    t1 = time.time()
    input = [([2,3,1,1,4], 2),
            ([2,3,0,1,4], 2),
            ([0], 0),
            ([1,2], 1),
            ([2,0,2,0,1], 2),
            ([1,2,3], 2),
            ([1,2,3,4,5], 3),
            ([3,4,3,2,5,4,3],3)]

    for i in input:
        a = jump(i[0])
        print(i[0], ", s/b: ", i[1], ", is: ", a)

    print("Total time: ", time.time() - t1)

if __name__=='__main__':
    main()
