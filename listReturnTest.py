'''
Python
Test returning a list with a list as an element
'''
from typing import List

def testFunc(s: List[int]) -> List[List[int]]:
    rs = s[0]
    print("rs: ", rs)

    return [[rs]]

def testFunc2(s: List[List[int]]) -> List[int]:
    return s[0]

def testFunc3(s: List[int]) -> List[str]:
    print("s: ", s)

    #return ['a', 'b', 'c']
    return s

def testFunc4(i: int) -> int:
    print("i + 1 = ", i + 1)

    return i + 1

def main() -> None:
    s = [1, 2, 3]

    a = testFunc(s)
    b = testFunc2(a)

    print("a: ", a)
    print("type(a): ", type(a))
    print("type(a[0]): ", type(a[0]))
    print("b: ", b)

    #print("testFunc3: ", testFunc3([1,2,3]))
    print("testFunc3: ", testFunc3(['a', 'b', 'c']))

    c = testFunc4('a')
    print("c: ", c)

if __name__=='__main__':
    main()
