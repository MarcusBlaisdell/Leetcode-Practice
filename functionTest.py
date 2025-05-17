'''
function test
'''
from typing import List

def func2(v: List) -> List:
    v.append((1,2))
    print("inside func2, v: ", v)

    return [1,7]

def func1() -> List:
    r = []
    v = []
    print("func1 v before: ", v)
    r = func2(v)
    print("func1 v after: ", v)

    return r

def main() -> None:
    a = func1()

    print("a: ", a)

if __name__=='__main__':
    main()
