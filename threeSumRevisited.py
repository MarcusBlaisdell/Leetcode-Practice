'''
Leetcode
3Sum
Medium

Given an integer array nums, return all the triplets [nums[i],
nums[j], nums[k]] such that i != j, i != k, and j != k, and
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets
does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.



Constraints:

    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5


'''
from typing import List

def twoSum(nums: List, t: int) -> List:
    r = []
    t = t * -1

    for i in nums:
        nums2 = nums[:]
        nums2.remove(i)
        if (t - i) in nums2:
            add = [i, t - i]
            add.sort()
            if (add) not in r:
                r.append(add)

    return r

def threeSum(nums: List) -> List:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        I can use two sum solution in combination with each
        integer, for each integer i in nums, run twoSum with (-1 * i)
        as the target
        Seems like a poor time complexity, but...
        '''
        r = []
        found = set()
        # if not enough integers, return empty list:
        if len(nums) < 3:
            return r

        # if only three integers, check if valid and return nums,
        # and empty list if not valid:
        if len(nums) == 3:
            if (nums[0] + nums[1] + nums[2]) != 0:
                return []
            else:
                r.append(nums)
                return r
        else:
            # more than 3 integers:
            for i in nums:
                # find all sets of two that sum to 0 with i:
                nums2 = nums[:]
                nums2.remove(i)
                n = twoSum(nums2, i)
                for j in n:
                    k = j[:]
                    k.append(i)
                    k.sort()
                    if k not in r:
                        r.append(k)

        return r


def main() -> None:
    # test threeSum:
    test = [([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
            ([0,1,1], []),
            ([0,0,0], [[0,0,0]]),
            ([1,2,-3],[[1,2,-3]]),
            ([-1, 1, 0, -2, 2, -3, 3],[[-1,1,0],[-2,2,0],[-3,3,0]])]

    for i in test:
        a = threeSum(i[0])
        print("s/b: ", i[1], ", is: ", a)
    '''
    # test twoSum:
    test = [([-1,0,1,2,-1,-4], [[-1,1]]),
            ([0,1,1], []),
            ([0,0,0], [[0,0]]),
            ([1,2,-3],[[]]),
            ([-1, 1, 0, -2, 2, -3, 3],[[-1,1],[-2,2],[-3,3]])]

    for i in test:
        a = twoSum(i[0], 0)
        print("s/b: ", i[1], ", is: ", a)
    '''

if __name__=='__main__':
    main()
