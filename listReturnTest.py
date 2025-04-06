'''
Python
Test returning a list with a list as an element
'''
from typing import List

def testFunc(s: List[int]) -> List[List[int]]:
    rs = s[0]
    print("rs: ", rs)

    # This shouldn't work, rs is an int,
    # [rs] is a List[int], return type is
    # supposed to be List[List[int]]
    return [[rs]]

def testFunc2(s: List[List[int]]) -> List[int]:
    return s[0]

def main() -> None:
    s = [1, 2, 3]

    a = testFunc(s)
    b = testFunc2(a)

    print("a: ", a)
    print("type(a): ", type(a))
    print("type(a[0]): ", type(a[0]))
    print("b: ", b)

if __name__=='__main__':
    main()
