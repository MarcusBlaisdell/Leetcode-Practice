'''
Linked List test

('the lists: ', [ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}, ListNode{val: 2, next: ListNode{val: 6, next: None}}])
('type(lists): ', <type 'list'>)

('j: ', 0, ', k: ', ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}})
('j: ', 1, ', k: ', ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}})
('j: ', 2, ', k: ', ListNode{val: 2, next: ListNode{val: 6, next: None}})

'''
import json
from typing import List

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def main() -> None:
    #head = [ListNode{val: 1}]
    #head = ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
    #, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}, ListNode{val: 2, next: ListNode{val: 6, next: None}}
    #head = ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}, ListNode{val: 2, next: ListNode{val: 6, next: None}}

    #input = [ListNode(1), ListNode(2)]
    input = [ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}, ListNode{val: 2, next: ListNode{val: 6, next: None}}]

    # read until left brace, then look for "val: ", get value,
    # when curly braces are all matched, start new list:
    for k in input:
        print("k: ", k)


    print("x: ", x)
    # print list:
    print("print list: ")
    curNode = head
    while curNode != None:
        print(curNode.val)
        curNode = curNode.next

if __name__=='__main__':
    main()
