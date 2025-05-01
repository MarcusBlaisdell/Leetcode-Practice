'''
Leetcode 4
Median of two sorted arrays
2025-04-29

Given two sorted arrays a1 and a2 of size m and n
respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: a1 = [1,3], a2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: a1 = [1,2], a2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''
from typing import List
import time

def findMedianSortedArrays(nums1: List, nums2: List) -> float:
    answer = 0.0
    medNum = (len(nums1) + len(nums2)) // 2
    if len(nums1) < len(nums2):
        a1 = nums1
        a2 = nums2
    elif len(nums2) < len(nums1):
        a1 = nums2
        a2 = nums1
    elif len(nums1) == len(nums2):
        if (nums1[0] > nums2[len(nums2)-1]):
            a1 = nums2
            a2 = nums1
        else:
            a1 = nums1
            a2 = nums2
    '''
    two possibilities, len(a1) + len(a2) is odd,
    len(a1) + len(a2) is even

    two pointers, Left Index for each array:
    l1, l2

    if a1[l1] <= a2[l2]:
    '''
    l1, l2 = 0, 0

    # Find starting lowest number, set to current number, c:
    if (len(a1) == 0):
        if (len(a2) > 0):
            c = a2[0]
            l2 = 1
        else:
            return 0
    elif (len(a2) == 0):
        if (len(a1) > 0):
            c = a1[0]
            l1 = 1
        else:
            return 0
    elif (a1[l1] < a2[l2]) or (a1[l1] == a2[l2]):
        c = a1[l1]
        if l1 < (len(a1) - 1):
            l1 = 1
    elif (a2[l2] < a1[l1]):
        c = a2[l2]
        if l2 < (len(a2) - 1):
            l2 = 1
    # Previous number will be last c before update, initialize to 0:
    p = 0
    # index starts at 1 since we already found array[0] value:
    i = 1

    # find next lowest number until median reached:
    # case 1: a1 has elements, a2 is empty:
    if (len(a1) > 0) and (len(a2) == 0):
        # just go through a1:
        for i in range(medNum):
            p = c
            c = a1[l1]
            if l1 < (len(a1) - 1):
                l1 += 1
        if (len(a1) % 2) == 1:
            return c
        else:
            return ((c + p) * 1.0) / 2
    # case 2: a2 has elements, a1 is empty:
    elif (len(a2) > 0) and (len(a1) == 0):
        # just go through a1:
        for i in range(medNum):
            p = c
            c = a2[l2]
            if l2 < (len(a2) - 1):
                l2 += 1
        if (len(a2) % 2) == 1:
            return c
        else:
            return ((c + p) * 1.0) / 2
    # case 3: a1 and a2 each have just one element
    elif (len(a1) == 1) and (len(a2) == 1):
        return ((a1[0] + a2[0]) * 1.0) / 2
    else:
        # The below assumes both a1 and a2 contain elements:
        while i <= medNum:
            #print("c: ", c, ", l1: ", l1, ", l2: ", l2, ", i: ", i)
            #time.sleep(1)
            # handle duplicates:
            if (l1 > 0) and (a1[l1] == a1[l1-1]):
                p = c
                c = a1[l1]
                if l1 < (len(a1) - 1) and (i < medNum):
                    l1 += 1
                i += 1

            #This is the master:
            elif ((l2 > 0) and (a2[l2] == a2[l2-1])) or (a2[l2] == c):
            # test1:
            #elif (l2 > 0) and ((a2[l2] == a2[l2-1]) or (a2[l2] == c)):
            # test2:
            #elif ((l2 > 0) and (a2[l2] == a2[l2-1])) or (l2 > 0 and (a2[l2] == c)):
            # test3:
            #elif (a2[l2] == c):
                p = c
                c = a2[l2]
                if l2 < (len(a2) - 1) and (i < medNum):
                    l2 += 1
                i += 1
            elif (a1[l1] > c) and (a2[l2] > c):
                p = c
                if (a1[l1] <= a2[l2]):
                    c = a1[l1]
                    if l1 < (len(a1) - 1) and (i < medNum):
                        l1 += 1
                    i += 1
                elif (a2[l2] < a1[l1]):
                    c = a2[l2]
                    if l2 < (len(a2) - 1) and (i < medNum):
                        l2 += 1
                    i += 1
            elif (a1[l1] > c) and (a2[l2] <= c):
                p = c
                c = a1[l1]
                if l1 < (len(a1) - 1) and (i < medNum):
                    l1 += 1
                i += 1
            elif (a2[l2] > c) and (a1[l1] <= c):
                p = c
                c = a2[l2]
                if l2 < (len(a2) - 1) and (i < medNum):
                    l2 += 1
                i += 1

        if ((len(a1) + len(a2)) % 2) == 1:
            return c
        else:
            # Leetcode wasn't doing float division,
            # had to force it by making numerator a float:
            #print("c: ", c, ", p: ", p)
            return ((c + p)*1.0) / 2

    return answer

def main() -> None:
    #test = [([3,4],[1,2],2.5)]
    #test = [([2,2,4,4],[2,2,2,4,4],2)]

    test = [([1,3],[2],2),
            ([1,2],[3],2),
            ([1,2,3,4],[5],3),
            ([1],[2,3,4,5],3),
            ([1,3],[2,4],2.5),
            ([1,2],[3,4],2.5),
            ([1,1],[1,1],1),
            ([0,0],[0,0],0),
            ([],[1],1),
            ([0,0,0,0,0],[-1,0,0,0,0,0,1],0),
            ([2,2,4,4],[2,2,2,4,4],2),
            ([],[2,3],2.5),
            ([100001],[100000],100000.5),
            ([2,3],[1],2),
            ([3,4],[1,2],2.5)]
    '''
    test = [([1,3],[2],2)]
    test = [([2,2,4,4],[2,2,2,4,4],2)]
    '''

    for i in test:
        a = findMedianSortedArrays(i[0], i[1])
        print("s/b: ", i[2], " - is: ", a)

if __name__=='__main__':
    main()
