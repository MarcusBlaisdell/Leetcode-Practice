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

110/110
Runtime beats 92.93%
Memory beats 84.73%
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
        i = 0 # index
        j = 0 # jump counter

        while i < (len(nums) - 1):
            if (i + nums[i]) >= (len(nums) - 1):
                return j + 1
            m = 0 # max val
            n = 0
            # find optimal jump position,
            # defined as:
            # position that gets farthest

            for k in range(1,nums[i] + 1):
                if ((i + k + nums[i + k]) > m) and (nums[i + k] != 0):
                    m = i + k + nums[i + k]
                    n = i + k # next index
            i = n
            j += 1

        return j

def main() -> None:
    t1 = time.time()
    correct = 0
    total = 0
    input = [([2,3,1,1,4], 2),
            ([2,3,0,1,4], 2),
            ([0], 0),
            ([1,2], 1),
            ([2,0,2,0,1], 2),
            ([1,2,3], 2),
            ([1,2,3,4,5], 3),
            ([3,4,3,2,5,4,3],3)]

    for i in input:
        total += 1
        a = jump(i[0])
        if a == i[1]:
            correct += 1
        print(i[0], ", s/b: ", i[1], ", is: ", a)

    print("Total: ", correct, " / ", total)
    print("Total time: ", time.time() - t1)

if __name__=='__main__':
    main()
