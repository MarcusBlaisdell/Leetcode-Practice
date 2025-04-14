'''
Leetcode 707
Implement a linked list:
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

    MyLinkedList() Initializes the MyLinkedList object.
    int get(int index) Get the value of the indexth node
       in the linked list. If the index is invalid,
       return -1.
    void addAtHead(int val) Add a node of value val before
        the first element of the linked list. After the
        insertion, the new node will be the first node of
        the linked list.
    void addAtTail(int val) Append a node of value val as
        the last element of the linked list.
    void addAtIndex(int index, int val) Add a node of value
        val before the indexth node in the linked list. If
        index equals the length of the linked list, the node
        will be appended to the end of the linked list. If
        index is greater than the length, the node will not
        be inserted.
    void deleteAtIndex(int index) Delete the indexth node in
        the linked list, if the index is valid.

'''

class MyLinkedList(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get(self, index) -> int:
        """
        :type index: int
        :rtype: int
        """
        for i in range(index):
            if self.next == None:
                return -1
            else:
                self = self.next
        return self.val

    def addAtHead(self, val: int):
        newNode = MyLinkedList(self.val, self.next)
        self.val = val
        self.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = MyLinkedList(val)
        while self.next != None:
            self = self.next
        self.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = MyLinkedList(val)
        for i in range(index - 1):
            if self.next == None:
                break
            else:
                self = self.next
        newNode.next = self.next
        self.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        for i in range(index - 1):
            if self == None:
                break
            else:
                self = self.next
        delNode = self.next
        self.next = self.next.next
        del delNode
# end class

def printList(head: MyLinkedList) -> None:
    iterNode = head
    while iterNode != None:
        print(iterNode.val)
        iterNode = iterNode.next
    del iterNode

def main() -> None:
    head = MyLinkedList(1)
    iterNode = head
    newNode = MyLinkedList(2)
    head.next = newNode

    print("Starting list:")
    printList(head)

    print("get(1):")
    print("head.get(1): ", head.get(1))

    print("Add at head:")
    head.addAtHead(0)
    printList(head)

    print("Add at tail:")
    head.addAtTail(4)
    printList(head)

    print("Add at index:")
    head.addAtIndex(2, 3)
    printList(head)

    print("Delete at index:")
    head.deleteAtIndex(2)
    printList(head)

if __name__=='__main__':
    main()
