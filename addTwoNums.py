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

Need to read through each list to the end, could use a stack
'''

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    stack1 = []
    stack2 = []
    retNode = ListNode()

    node1 = l1
    stack1.append(node1.val)
    while node1.next != None:
        node1 = node1.next
        stack1.append(node1.val)

    node2 = l2
    stack2.append(node2.val)
    while node2.next != None:
        node2 = node2.next
        stack2.append(node2.val)

    print("stack1: ", stack1)
    print("stack2: ", stack2)

    carry = 0

    add1 = stack1.pop()
    add2 = stack2.pop()
    val = (add1 + add2 + carry) % 10
    carry = (add1 + add2) // 10
    retNode.val = val
    moveNode = retNode
    nextNode = ListNode()
    retNode.next = nextNode

    for i in range(len(stack1)):

        add1 = stack1.pop()
        add2 = stack2.pop()
        val = (add1 + add2 + carry) % 10
        carry = (add1 + add2) // 10
        nextNode.val = val
        newNode = ListNode()
        nextNode.next = newNode
        nextNode = nextNode.next

    return retNode


def main() -> None:
    node1 = ListNode(2)
    node1.next = ListNode(4)
    node1.next.next = ListNode(3)

    node2 = ListNode(5)
    node2.next = ListNode(6)
    node2.next.next = ListNode(4)

    retNode = addTwoNumbers(node1, node2)
    while retNode.next != None:
        print(retNode.val)
        retNode = retNode.next

if __name__=='__main__':
    main()
