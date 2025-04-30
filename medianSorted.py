'''
Leetcode 4
Median of two sorted arrays
2025-04-29

Given two sorted arrays nums1 and nums2 of size m and n
respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''
from typing import List

def findMedianSortedArrays(nums1: List, nums2: List) -> float:
    answer = 0.0
    medNum = (len(nums1) + len(nums2)) // 2
    '''
    two possibilities, len(nums1) + len(nums2) is odd,
    len(nums1) + len(nums2) is even

    two pointers, Left Index for each array:
    l1, l2

    if nums1[l1] <= nums2[l2]:
    '''
    l1, l2 = 0, 0

    # Find starting lowest number, set to current number, c:
    if (nums1[l1] < nums2[l2]) or (nums1[l1] == nums2[l2]):
        c = nums1[l1]
        if l1 < (len(nums1) - 1):
            l1 += 1
    elif (nums2[l2] < nums1[l1]):
        c = nums2[l2]
        if l2 < (len(nums2) - 1):
            l2 += 1
    # Previous number will be last c before update, initialize to 0:
    p = 0
    # index starts at 1 since we already found array[0] value:
    i = 1

    # find next lowest number until median reached:
    while i <= medNum:
        if (nums1[l1] > c) and (nums2[l2] > c):
            p = c
            if (nums1[l1] < nums2[l2]):
                c = nums1[l1]
                if l1 < (len(nums1) - 1) and (i < medNum):
                    l1 += 1
                i += 1
            elif (nums2[l2] < nums1[l1]):
                c = nums2[l2]
                if l2 < (len(nums2) - 1) and (i < medNum):
                    l2 += 1
                i += 1
        elif (nums1[l1] > c) and (nums2[l2] <= c):
            p = c
            c = nums1[l1]
            if l1 < (len(nums1) - 1) and (i < medNum):
                l1 += 1
            i += 1
        elif (nums2[l2] > c) and (nums1[l1] <= c):
            p = c
            c = nums2[l2]
            if l2 < (len(nums2) - 1) and (i < medNum):
                l2 += 1
            i += 1

    if ((len(nums1) + len(nums2)) % 2) == 1:
        return c
    else:
        return (c + p) / 2

    return answer

def main() -> None:
    test = [([1,3],[2],2),
            ([1,2],[3],2),
            ([1,2,3,4],[5],3),
            ([1],[2,3,4,5],3),
            ([1,3],[2,4],2.5),
            ([1,2],[3,4],2.5)]
    '''
    test = [([1,3],[2],2)]
    test = [([1,2,3,4],[5],3)]
    '''

    for i in test:
        a = findMedianSortedArrays(i[0], i[1])
        print("s/b: ", i[2], " - is: ", a)

if __name__=='__main__':
    main()
