'''
Leetcode 33
Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot
unknown to you.
E.G. [0,1,2,4,5,6,7] becomes [4,5,6,7,0,1,2]

Given a target value to search, if found in the array, return its
index, otherwise, return -1.

May assume no duplicates in the array
Runtime complexity must be in the order of O(logn)

E.G.
[4,5,6,7,0,1,2], target = 0
returns 4
binary search
while left index < right index
[4,5,6,7,0,1,2], 7 elements, 7/2 = 3, check nums[3]
nums[3] = 7, 7 > 3,
decide to go right or left, first, check beginning index,
if nums[0] > target & < current, go right,
4 > 0 & 4 < 7, go right, (7-3) = 4 / 2 = 2 + 3 = 5
nums[5] = 1
1 > 0, left index = 3, nums[3] > target, current < left index, go left
(5 - 3) = 2 / 2 = 1, 5 - 1 = 4
nums[4] = 0, 0 matches target, return index

[1,2,4,5,6,7,0]
[6,7,0,1,2,4,5]
[4,5,6,7,1,2,3], target = 0
'''
from typing import List

def search(nums: List, target: int) -> int:
    # check end points:
    if nums[0] == target:
        return 0
    if nums[len(nums) - 1] == target:
        return len(nums) - 1

    l,r = 0, (len(nums) - 1)
    cur = (r - l) // 2

    while l < (r - 1):
        if nums[cur] == target:
            return cur
        elif (target > nums[l]) & (target < nums[cur]):
            r = cur
            cur = (((r - l) // 2) + l)
        elif (target > nums[cur]) & (target < nums[r]):
            l = cur
            cur = (((r - l) // 2) + l)
        # if target less than current position,
        # and left index less than current position,
        # move right:
        elif (target < nums[cur]) & (target < nums[l]) & (nums[l] < nums[cur]):
            l = cur
            cur = (((r - l) // 2) + l)
        # if target less than current position,
        # and left index greater than current position,
        # move left
        elif (target < nums[cur]) & (target < nums[l]) & (nums[l] > nums[cur]):
            r = cur
            cur = (((r - l) // 2) + l)
        # if target greater than current position,
        # and left index < current index,
        # move right
        elif (target > nums[cur]) & (target > nums[l]) & (nums[l] < nums[cur]):
            l = cur
            cur = (((r - l) // 2) + l)
        # if target greater than current position,
        # and left index > current index,
        # move left
        elif (target > nums[cur]) & (target > nums[l]) & (nums[l] > nums[cur]):
            r = cur
            cur = (((r - l) // 2) + l)

    return -1

def main() -> None:
    '''
    nums = [4,5,6,7,0,1,2]
    target = 0
    '''
    input = [([4,5,6,7,0,1,2],0,4),
            ([1,2,4,5,6,7,0],0,6),
            ([6,7,0,1,2,4,5],0,2),
            ([4,5,6,7,1,2,3],0,-1),
            ([4,5,6,7,0,1,2],3,-1)]

    for i in input:
        answer = search(i[0], i[1])
        print("Answer s/b: ", i[2], " : ", answer)

if __name__=='__main__':
    main()
