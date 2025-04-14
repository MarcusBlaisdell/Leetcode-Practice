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

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def get(self, index) -> int:
        """
        :type index: int
        :rtype: int
        """
        for i in range(index):
            if self == None:
                return -1
            else:
                self = self.next
        return self.val

    def addAtHead(self, val: int):
        # if list is empty:
        if (self.val == None) & (self.next == None):
            self.val = val
        else:
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
        # edge case, list has only 1 element:
        if (self.next == None) & (self.val != None):
            self.val = None
        # edge case, list is empty, do nothing:
        elif (self.val == None) & (self.next == None):
            pass
        else:
            for i in range(index - 1):
                if self == None:
                    break
                else:
                    self = self.next
            # Edge case: index is end of list:
            if self.next == None:
                del self
            else:
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
    '''
    "MyLinkedList",[], []
    "addAtHead",[1], [1,[]]
    "addAtTail",[3], [1,[],3]
    "addAtIndex",[1,2], [1,2,[],3]
    "get",[1], return 2
    "deleteAtIndex",[1], [1,[],3]
    "get",[1] return null
    '''
    '''
    # Test case 1
    head = MyLinkedList()
    head.addAtHead(1)
    head.addAtTail(3)
    head.addAtIndex(1,2)
    print(head.get(1))
    head.deleteAtIndex(1)
    print(head.get(1))
    # end test case 1
    '''

    '''
    # test case 2, delete at index, index is end of list:
    head = MyLinkedList(1)
    #head.addAtTail(2)
    print("before:")
    printList(head)
    head.deleteAtIndex(0)
    print("after")
    printList(head)
    head.deleteAtIndex(0)
    print("after")
    printList(head)
    '''
    #testcase 3:

    head = MyLinkedList()
    head.addAtHead(7)
    print("head.addAtHead(7) s/b: [7]")
    printList(head)
    head.addAtHead(2)
    print("head.addAtHead(2) s/b [2,7]")
    printList(head)
    head.addAtHead(1)
    print("head.addAtHead(1) s/b [1,2,7]")
    printList(head)
    head.addAtIndex(3,0)
    print("head.addAtIndex(3,0) s/b [1,2,7,0]")
    printList(head)
    head.deleteAtIndex(2)
    print("head.deleteAtIndex(2) s/b [1,2,0]")
    printList(head)
    head.addAtHead(6)
    print("head.addAtHead(6) s/b: [6,1,2,0]")
    printList(head)
    head.addAtTail(4)
    print("head.addAtTail(4) s/b: [6,1,2,0,4]")
    printList(head)
    print("head.get(4) s/b 4: ")
    print(head.get(4))
    head.addAtHead(4)
    print("head.addAtHead(4)s/b [4,6,1,2,0,4]")
    printList(head)
    head.addAtIndex(5,0)
    print("head.addAtIndex(5,0) s/b [4,6,1,2,0,0,4]")
    printList(head)
    head.addAtHead(6)
    print("head.addAtHead(6) s/b: [6,4,6,1,2,0,0,4]")
    printList(head)


    '''
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
    '''

if __name__=='__main__':
    main()
