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

    # Find starting lowest number:
    s = min(nums1[0], nums2[0])
    i = 0

    # find next lowest number until median reached:
    while i <= medNum:
        print("i: ", i, ", s: ", s, ", medNum: ", medNum)
        if (nums1[l1] < nums2[l2]):
            s = nums1[l1]
            i += 1
            if (l1 < len(nums1) - 1):
                l1 += 1
        if (nums2[l2] < nums1[l1]):
            s = nums2[l2]
            i += 1
            if (l2 < len(nums2) - 1):
                l2 += 1
        elif (nums1[l1] == nums2[l2]):
            s = nums1[l1]
            l1 += 1
            l2 += 1
            i += 2
        elif (nums1[l1] == nums2[l2]):
            if (l1 < len(nums1) - 1):
                l1 += 1
            if (l2 < len(nums2) - 1):
                l2 += 1
    if ((len(nums1) + len(nums2)) % 2) == 1:
        answer = s
    else:
        #find next number:
        print("nums1[l1]: ", nums1[l1], ", nums2[l2]: ", nums2[l2])
        if (nums1[l1] < nums2[l2]):
            t = nums1[l1]
        if (nums2[l2] < nums1[l1]):
            t = nums2[l2]
        if (nums1[l1] == nums2[l2]):
            t = nums1[l1]
        print("s: ", s, ", t: ", t)
        answer = (s + t) / 2

    return answer

def main() -> None:
    input = [([1,3],[2],2),
            ([1,2],[3],2),
            ([1,2,3,4],[5],3),
            ([1],[2,3,4,5],3),
            ([1,3],[2,4],2.5)]
    '''

    input = [([1,3],[2],2)]
    '''

    for i in input:
        a = findMedianSortedArrays(i[0], i[1])
        print("s/b: ", i[2], " - is: ", a)

if __name__=='__main__':
    main()
