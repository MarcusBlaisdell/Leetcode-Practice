'''
Leetcode 206
April 12, 2025
Reverse Linked List
1 -> 2 -> 3 -> 4 -> 5
c    n    h

'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    # edge cases:
    # list is empty:
    if head == None:
        return head
    # only one node in linked list:
    if head.next == None:
        return head
    # only two items in list:
    if head.next.next == None:
        nextNode = head.next
        nextNode.next = head
        head.next = None
        head = nextNode
        return head
    # if 3 or more nodes:
    curNode = head
    nextNode = curNode.next
    head = nextNode.next
    curNode.next = None

    while head != None:
        nextNode.next = curNode
        curNode = nextNode
        nextNode = head
        head = head.next
    nextNode.next = curNode
    curNode = nextNode
    head = curNode

    return head

def main() -> None:
    head = ListNode(1)
    curNode = head

    for i in range(2,6):
        tmp = ListNode(i)
        curNode.next = tmp
        curNode = curNode.next

    head = reverseList(head)

    curNode = head

    while curNode != None:
        print("curNode.val: ", curNode.val)
        curNode = curNode.next

if __name__=='__main__':
    main()
