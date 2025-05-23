'''
Leetcode 19
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from
the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]



Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz



Follow up: Could you do this in one pass?

Runtime beats 100%
Memory beats 20.10%

'''
import time

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#class Solution(object):
def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    # need to find out how many nodes:
    i = 0
    nextNode = head
    while nextNode != None:
        nextNode = nextNode.next
        i += 1

    theNode = i - n
    if i == 1:
        del head
        return None

    if theNode == 0:
        head = head.next
        return head

    nextNode = head

    for i in range(i - n - 1):
        nextNode = nextNode.next
    #toDel = nextNode.next
    nextNode.next = nextNode.next.next
    #del nextNode.next

    return head

def main() -> None:
    t1 = time.time()

    test = [([1,2,3,4,5], 2, [1,2,3,5]),
            ([1], 1, []),
            ([1,2], 1, [1]),
            ([1,2], 2, [2])]

    for i in test:
        # build List:
        # Create Head Node:
        head = ListNode(i[0][0])
        nextNode = head

        for j in range(1,len(i[0])):
            newNode = ListNode(i[0][j])
            nextNode.next = newNode
            nextNode = newNode

        head = removeNthFromEnd(head, i[1])

        print("test ", i, ":")
        # print the list:
        if head == None:
            print("s/b: [], is: ", [])
        else:
            nextNode = head
            printList = []
            while nextNode != None:
                printList.append(nextNode.val)
                nextNode = nextNode.next
            print("s/b: ", i[2], ", is: ", printList)


if __name__=='__main__':
    main()
