'''
Leetcode 322
Coin Change
April 08, 2025
Given coins of different denominations, and a total amount of money,
write a function to compute the fewest number of coins needed
mod operator
'''
from typing import List

def coinChange(i: List[int], a: int) -> int:
    res = 0

    while a != 0:
        c = max(i)
        i.remove(max(i))
        res += a // c
        a = a % c

    return res

def main() -> None:
    input = [([1,2,5],11)]

    for i, a in input:
        a = coinChange(i, a)
        print("answer: ", a)


if __name__=='__main__':
    main()
