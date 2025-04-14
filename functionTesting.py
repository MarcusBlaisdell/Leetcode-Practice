'''
Python function test
'''
from typing import List

def func1(a: int) -> None:
    print("func1:")
    a += 1
    print(a)

def func2(l: List[int]) -> None:
    for i in range(len(l)):
        l[i] += 1

def main() -> None:
    a = 1
    func1(a)
    print("main: ", a)

    l = [1,2,3]
    print("before:")
    for i in l:
        print(i)
    func2(l)
    print("after:")
    for i in l:
        print(i)

if __name__=='__main__':
    main()
