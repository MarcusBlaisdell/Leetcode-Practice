'''
Leetcode 2
Add Two Numbers
April 09, 2025
Given two non-empty linked lists of non-negative single integers,
stored in reverse order,
add the two numbers and return it as a linked list
E.G.
(2 -> 4 -> 3) +
(5 -> 6 -> 4) =
(7 -> 0 -> 8)

3 + 4 = 7
4 + 6 = 10, store 0, carry the 1,
2 + 5 = 7 + 1 = 8

'''

# This is the node class provided in the example:
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # To process and traverse a linked list, need two nodes:
    # a root node, and a current node:
    rootNode = ListNode()
    curNode = rootNode

    carry = 0

    #l1 and l2 may not be the same size:
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        # set val:
        curNode.val = (val1 + val2 + carry) % 10
        # get new carry value:
        carry = (val1 + val2 + carry) // 10
        # create a new node, set it to current node's next:
        curNode.next = ListNode()
        # move to new node:
        curNode = curNode.next
        # increment input list(s):
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # return the root node:
    return rootNode

def main() -> None:
    node1 = ListNode(2)
    node1.next = ListNode(4)
    node1.next.next = ListNode(3)

    node2 = ListNode(5)
    node2.next = ListNode(6)
    node2.next.next = ListNode(4)

    rootNode = addTwoNumbers(node1, node2)
    while rootNode.next != None:
        print(rootNode.val)
        rootNode = rootNode.next

if __name__=='__main__':
    main()
