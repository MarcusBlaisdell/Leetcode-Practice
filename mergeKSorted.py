'''
Leetcode 23
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list
is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
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

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    :type lists: List[Optional[ListNode]]
    :rtype: Optional[ListNode]
    """
    print("lists: ", lists)
    if len(lists) == 0:
        head = ListNode(None)
        return head
    if (len(lists) == 1) and (len(lists[0]) == 0):
        head = ListNode(None)
        return head
    # build the lists, store heads in a List:
    llList = []

    for l in lists:
        if len(l) > 0:
            head = ListNode(l[0])
            curNode = head
            for i in range(1,len(l)):
                nextNode = ListNode(l[i])
                curNode.next = nextNode
                curNode = curNode.next
            llList.append(head)

    # sort:

    # create List, hindex, to hold current LL positions,
    # start at zero:
    # create List, minList, to hold the current LL position value:
    hindex = []
    minList = []
    for h in llList:
        if h.val != None:
            hindex.append(0)
            minList.append(h.val)
        else:
            hindex.append(float('inf'))

    # initialize, get all first values,
    # determine smallest,
    # create head node with smallest value,
    # increment position index, node, etc.
    minN = float('inf')
    minIndex = 0
    for i in range(len(minList)):
        if minList[i] < minN:
            minN = minList[i]
            minIndex = i
    head = ListNode(minN)
    nextNode = head
    if llList[minIndex].next != None:
        llList[minIndex] = llList[minIndex].next
        hindex[i] += 1
        minList[i] += 1
    else:
        hindex[i] = float('inf')
        minList[i] = float('inf')

    while min(hindex) != float('inf'):
        minN = float('inf')
        minIndex = 0
        # get min value found so far:
        for i in range(len(minList)):
            if minList[i] < minN:
                minN = minList[i]
                minIndex = i
        # create new node with min value,
        # increment respective list pointer
        newNode = ListNode(minN)
        print("minN: ", minN, ", newNode.val: ", newNode.val)
        nextNode.next = newNode
        nextNode = nextNode.next
        if llList[minIndex].next != None:
            llList[minIndex] = llList[minIndex].next
            hindex[i] += 1
            minList[i] += 1
        else:
            hindex[i] = float('inf')
            minList[i] = float('inf')

    return head


    '''
    # print each list:
    for h in llList:
        printList = []
        while h != None:
            printList.append(h.val)
            h = h.next
        print("printlist: ", printList)
    '''


def main() -> None:
    t1 = time.time()

    test = [([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
            ([], []),
            ([[]], [])]

    for i in test:
        head = mergeKLists(i[0])
        printList = []
        while head != None:
            printList.append(head.val)
            head = head.next
        print("s/b: ", i[1], ", is: ", printList)

    print("Total time: ", time.time() - t1 )


if __name__=='__main__':
    main()
