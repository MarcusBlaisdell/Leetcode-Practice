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
    '''
    two possibilities, len(nums1) + len(nums2) is odd,
    len(nums1) + len(nums2) is even

    two pointers, Left Index for each array:
    l1, l2

    if nums1[l1] <= nums2[l2]:
    '''
    l1, l2 = 0, 0


    while (l1 + l2) < ((len(nums1) + len(nums2)) // 2):
        if nums1[l1] <= nums2[l2]:
            if l1 + 1 < len(nums1):
                l1 += 1
        else:
            if l2 + 1 < len(nums2):
                l2 += 1

    # if total size is odd:
    if (((len(nums1) + len(nums2)) % 2) == 1):
        answer = min(nums1[l1], nums2[l2])
    else:
        answer = (max(nums1[l1], nums2[l2]) + max(nums1[l1+1], nums2[l2+1])) / 2

    return answer

def main() -> None:
    input = [([1,3],[2],2),
            ([1,2],[3],2),
            ([1,2,3,4],[5],3),
            ([1],[2,3,4,5],3),
            ([1,3],[2,4],2.5)]

    for i in input:
        a = findMedianSortedArrays(i[0], i[1])
        print("s/b: ", i[2], " - is: ", a)

if __name__=='__main__':
    main()
