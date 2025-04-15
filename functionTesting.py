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

# iterate through list to element n
def func3(l: List, n: int) -> None:
    for i in range(n):
        if i >= len(l):
            break
        print(l[i])

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

    print("func3, iterate through list to n:")
    l = [1,2,3,4,5]
    func3(l, 6)

if __name__=='__main__':
    main()
