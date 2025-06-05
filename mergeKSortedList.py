'''
Leetcode 23
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list
is sorted in ascending order.

Merge all the linked-lists into one sorted list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []



Constraints:

    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 10^4.


'''
import time

def mergeKLists(lists):
    """
    :type lists: List[Optional[ListNode]]
    :rtype: Optional[ListNode]
    """
    # handle empty lists:
    print("lists: ", lists)
    if len(lists) == 0:
        return []
    if (len(lists) == 1) and (len(lists[0]) == 0):
        return []

    ret = []

    # sort:
    # need pointers for each list:
    pointers = []
    total = 0
    for i in lists:
        total += len(i)
    for x in lists:
        pointers.append(0)

    # check values in each pointer to find smallest,
    # record its index,
    # add value to return list,
    # and increment it's pointer
    while len(ret) < total:
        minN = float('inf')
        curIndex = 0
        for i in range(len(pointers)):
            if pointers[i] < len(lists[i]):
                if lists[i][pointers[i]] < minN:
                    minN = lists[i][pointers[i]]
                    curIndex = i
        ret.append(lists[curIndex][pointers[curIndex]])
        pointers[curIndex] += 1

        print("ret: ", ret, ", pointers: ", pointers)

    return ret

def main() -> None:
    t1 = time.time()

    test = [([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
            ([], []),
            ([[]], [])]

    for i in test:
        a = mergeKLists(i[0])
        print("s/b: ", i[1], ", is: ", a)

    print("Total time: ", time.time() - t1 )


if __name__=='__main__':
    main()
