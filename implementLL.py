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
        # edge cases:
        # list is empty:
        if (self.val == None):
            return -1
        for i in range(index + 1):
            # index beyond list length:
            if self == None:
                return -1
            # index at last node:
            elif i == index:
                return self.val
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
        # edge case, list is empty:
        if (self.val == None) & (self.next == None):
            self.val = val
        else:
            newNode = MyLinkedList(val)
            while self.next != None:
                self = self.next
            self.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        # edge case, list is empty, index is 0:
        if (self.val == None) & (self.next == None) & (index == 0):
            self.val = val
        # insert at index 0:
        elif (index == 0):
            newNode = MyLinkedList(self.val,self.next)
            self.val = val
            self.next = newNode
        # edge case, list is empty, index is not zero:
        elif (self.val == None) & (index > 0):
            pass
        else:
            newNode = MyLinkedList(val)
            for i in range(index - 1):
                if self.next == None:
                    break
                else:
                    self = self.next
            newNode.next = self.next
            self.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        # edge case, index is zero, list has more than 1 element:
        if (index == 0) & (self.next != None):
            delNode = self.next
            self.val = delNode.val
            self.next = delNode.next
            del delNode
        else:
            # edge case, list has only 1 element:
            if (self.next == None) & (self.val != None) & (index == 0):
                self.val = None
            # edge case, list is empty, do nothing:
            elif (self.val == None) & (self.next == None):
                pass
            else:
                # index greater than 0, list has more than 1 element:
                for i in range(index - 1):
                    # This should handle going beyond list:
                    if self == None:
                        break
                    else:
                        self = self.next
                # Edge case: index is end of list:
                if (self != None):
                    if (self.next == None):
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
    print("head.addAtHead(1), s/b: [1]")
    printList(head)
    head.addAtTail(3)
    print("head.addAtTail(3), s/b: [1,3]")
    printList(head)
    head.addAtIndex(1,2)
    print("head.addAtIndex(1,2), s/b: [1,2,3]")
    printList(head)
    print("head.get(1), s/b: 2")
    print(head.get(1))
    head.deleteAtIndex(1)
    print("head.deleteAtIndex(1), s/b: [1,3]")
    printList(head)
    print("head.get(1), s/b: 3")
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
    '''
    head = MyLinkedList()
    head.addAtHead(7)
    head.addAtHead(2)
    head.addAtHead(1)
    head.addAtIndex(3,0)
    head.deleteAtIndex(2)
    head.addAtHead(6)
    head.addAtTail(4)
    head.get(4)
    head.addAtHead(4)
    head.addAtIndex(5,0)
    head.addAtHead(6)
    '''
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
    #testcase 2
    '''
    ["MyLinkedList", [],
    "addAtHead",[7],
    "addAtHead",[2],
    "addAtHead",[1],
    "addAtIndex",[3,0],
    "deleteAtIndex",[2],
    "addAtHead",[6],
    "addAtTail",[4],
    "get",[4],
    "addAtHead",[4],
    "addAtIndex",[5,0],
    "addAtHead"],[6]
    [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    '''
    '''
    head = MyLinkedList()
    head.addAtHead(7)
    print("addAtHead(7) s/b: [7]")
    printList(head)
    head.addAtHead(2)
    print("addAtHead(7) s/b: [2,7]")
    printList(head)
    head.addAtHead(1)
    print("head.addAtHead(1) s/b: [1,2,7]")
    printList(head)
    head.addAtIndex(3,0)
    print("head.addAtIndex(3,0) s/b: [1,2,7,0]")
    printList(head)
    head.deleteAtIndex(2)
    print("head.deleteAtIndex(2) s/b: [1,2,0]")
    head.addAtHead(6)
    print("head.addAtHead(6) s/b: [6,1,2,0]")
    printList(head)
    head.addAtTail(4)
    print("head.addAtTail(4) s/b: [6,1,2,0,4]")
    printList(head)
    print("head.get(4) s/b: 4")
    print(head.get(4))
    head.addAtHead(4)
    print("head.addAtHead(4) s/b: [4,6,1,2,0,4]")
    printList(head)
    head.addAtIndex(5,0)
    print("head.addAtIndex(5,0) s/b: [4,6,1,2,0,0,4]")
    printList(head)
    head.addAtHead(6)
    print("head.addAtHead(6) s/b: [6,4,6,1,2,0,0,4]")
    printList(head)
    '''

    # testcase 5:
    '''
    ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
    [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    ["MyLinkedList",[],
    "addAtHead",[7],
    "addAtHead",[2],
    "addAtHead",[1],
    "addAtIndex",[3,0],
    "deleteAtIndex",[2],
    "addAtHead",[6],
    "addAtTail",[4],
    "get",[4],
    "addAtHead",[4],
    "addAtIndex",[5,0],
    "addAtHead",[6]]
    '''
    '''
    head = MyLinkedList()
    head.addAtHead(7)
    print("head.addAtHead(7) s/b: [7]")
    printList(head)
    head.addAtHead(2)
    print("head.addAtHead(2) s/b: [2,7]")
    printList(head)
    head.addAtHead(1)
    print("head.addAtHead(1) s/b: [1,2,7]")
    printList(head)
    head.addAtIndex(3,0)
    print("head.addAtIndex(3,0) s/b: [1,2,7,0]")
    printList(head)
    head.deleteAtIndex(2)
    print("head.deleteAtIndex(2) s/b: [1,2,0]")
    printList(head)
    head.addAtHead(6)
    print("head.addAtHead(6) s/b: [6,1,2,0]")
    printList(head)
    head.addAtTail(4)
    print("head.addAtTail(4) s/b: [6,1,2,0,4]")
    printList(head)
    print("head.get(4) s/b: 4")
    print(head.get(4))
    head.addAtHead(4)
    print("head.addAtHead(4) s/b: [4,6,1,2,0,4]")
    printList(head)
    head.addAtIndex(5,0)
    print("head.addAtIndex(5,0) s/b: [4,6,1,2,0,0,4]")
    printList(head)
    "addAtHead",[6]
    head.addAtHead(6)
    print("head.addAtHead(6) s/b: [6,4,6,1,2,0,0,4]")
    printList(head)
    '''
    '''
    ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
    [[],[0,10],[0,20],[1,30],[0]]
    ["MyLinkedList", [],
    "addAtIndex",[0,10],
    "addAtIndex",[0,20],
    "addAtIndex",[1,30],
    "get",[0]]
    '''
    '''
    # testcase 53
    head = MyLinkedList()
    head.addAtIndex(0,10)
    print("head.addAtIndex(0,10) s/b: [10]")
    printList(head)
    head.addAtIndex(0,20)
    print("head.addAtIndex(0,20) s/b: [20,10]")
    printList(head)
    "addAtIndex",[1,30],
    head.addAtIndex(1,30)
    print("head.addAtIndex(1,30) s/b: [20,30,10]")
    printList(head)
    print("head.get(0), s/b: 20")
    print(head.get(0))
    '''

    '''
    ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
    [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
    ["MyLinkedList", [],
    "addAtHead",[2],
    "deleteAtIndex",[1],
    "addAtHead",[2],
    "addAtHead",[7],
    "addAtHead",[3],
    "addAtHead",[2],
    "addAtHead",[5],
    "addAtTail",[5],
    "get",[5],
    "deleteAtIndex",[6],
    "deleteAtIndex",[4]]
    '''
    '''
    # testcase 25
    head = MyLinkedList()
    head.addAtHead(2)
    print("head.addAtHead(2), s/b: [2]")
    printList(head)
    head.deleteAtIndex(1)
    print("head.deleteAtIndex(1), s/b: [2]")
    printList(head)
    head.addAtHead(2)
    print("head.addAtHead(2), s/b: [2,2]")
    printList(head)
    head.addAtHead(7)
    print("head.addAtHead(7), s/b: [7,2,2]")
    printList(head)
    head.addAtHead(3)
    print("head.addAtHead(3), s/b: [3,7,2,2]")
    printList(head)
    head.addAtHead(2)
    print("head.addAtHead(2), s/b: [2,3,7,2,2]")
    printList(head)
    head.addAtHead(5)
    print("head.addAtHead(5), s/b: [5,2,3,7,2,2]")
    printList(head)
    head.addAtTail(5)
    print("head.addAtTail(5), s/b: [5,2,3,7,2,2,5]")
    printList(head)
    print("head.get(5), s/b: 2")
    print(head.get(5))
    head.deleteAtIndex(6)
    print("head.deleteAtIndex(6), s/b: [5,2,3,7,2,2]")
    printList(head)
    head.deleteAtIndex(4)
    print("head.deleteAtIndex(4) s/b: [5,2,3,7,2]")
    printList(head)
    '''

    '''
    # testcase 62
    ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    [[],[1],[3],[1,2],[1],[0],[0]]
    ["MyLinkedList",[]
    "addAtHead",[1],
    "addAtTail",[3],
    "addAtIndex",[1,2],
    "get",[1],
    "deleteAtIndex",[0],
    "get",[0]]

    '''
    '''
    # testcase 62
    head = MyLinkedList()
    head.addAtHead(1)
    print("head.addAtHead(1), s/b: [1]")
    printList(head)
    head.addAtTail(3)
    print("head.addAtTail(3), s/b: [1,3]")
    printList(head)
    head.addAtIndex(1,2)
    print("head.addAtIndex(1,2), s/b: [1,2,3]")
    printList(head)
    print("head.get(1), s/b: 2")
    print(head.get(1))
    "deleteAtIndex",[0],
    head.deleteAtIndex(0)
    print("head.deleteAtIndex(0), s/b: [2,3]")
    printList(head)
    print("head.next: ", head.next)
    print("head.get(0), s/b: 2")
    print(head.get(0))
    '''

    '''
    # testcase 63:
    ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
    [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]
    ["MyLinkedList",[],
    "addAtHead",[1],
    "addAtTail",[3],
    "addAtIndex",[1,2],
    "get",[1],
    "deleteAtIndex",[1],
    "get",[1],
    "get",[3],
    "deleteAtIndex",[3],
    "deleteAtIndex",[0],
    "get",[0],
    "deleteAtIndex",[0],
    "get",[0]]

    '''
    '''
    # testcase 63
    head = MyLinkedList()
    head.addAtHead(1)
    print("head.addAtHead(1), s/b: [1]")
    printList(head)
    head.addAtTail(3)
    print("head.addAtTail(3), s/b: [1,3]")
    printList(head)
    head.addAtIndex(1,2)
    print("head.addAtIndex(1,2), s/b: [1,2,3]")
    printList(head)
    print("head.get(1), s/b: 2")
    print(head.get(1))
    print("list s/b: [1,2,3]")
    printList(head)
    head.deleteAtIndex(1)
    print("head.deleteAtIndex(1), s/b: [1,3]")
    print(head)
    print("head.get(1), s/b: 3")
    print(head.get(1))
    print("head.get(3), s/b: -1")
    print(head.get(3))
    head.deleteAtIndex(3)
    print("head.deleteAtIndex(3), s/b: [1,3]")
    printList(head)
    head.deleteAtIndex(0)
    print("head.deleteAtIndex(0), s/b: [3]")
    printList(head)
    print("head.get(0), s/b: 3")
    print(head.get(0))
    head.deleteAtIndex(0)
    print("head.deleteAtIndex(0), s/b: []")
    printList(head)
    print("head.get(0), s/b: -1")
    print(head.get(0))
    '''
    '''
    # testcase 65
    ["MyLinkedList","addAtIndex","addAtIndex","addAtTail","get","deleteAtIndex","get"]
    [[],[2,1],[3,4],[1],[0],[0],[0]]
    ["MyLinkedList",[[]],
    "addAtIndex",[2,1],
    "addAtIndex",[3,4],
    "addAtTail",[1],
    "get",[0],
    "deleteAtIndex",[0],
    "get",[0]]

    '''
    # testcase 65:
    head = MyLinkedList()
    head.addAtIndex(2,1)
    print("head.addAtIndex(2,1), s/b: []")
    printList(head)
    head.addAtIndex(3,4)
    print("head.addAtIndex(3,4), s/b: []")
    printList(head)
    head.addAtTail(1)
    print("head.addAtTail(1), s/b: [1]")
    printList(head)
    "get",[0],
    print("head.get(0), s/b: 1")
    print(head.get(0))
    head.deleteAtIndex(0)
    print("head.deleteAtIndex(0), s/b: []")
    printList(head)
    print("head.get(0), s/b: -1")
    print(head.get(0))

    '''
    # My initial tests:
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
