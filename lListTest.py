'''
Linked List test
'''
class Node(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def main() -> None:
    # build list in for loop:
    # initialize head node:
    head = Node(0)
    curNode = head

    # build list using a for loop:
    for i in range(1,5):
        newNode = Node(i)
        curNode.next = newNode
        curNode = curNode.next

    # print list:
    print("print list: ")
    curNode = head
    while curNode != None:
        print(curNode.val)
        curNode = curNode.next

if __name__=='__main__':
    main()
