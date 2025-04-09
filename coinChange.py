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
    input = [[([1,2,5],11), 3],
            [([1,2,5], 12), 3],
            [([1,2,5], 13), 4],
            [([1,2,5], 14), 4],
            [([1,2,5], 15), 3],
            [([1,2,5], 16), 4],
            [([1,2,5], 17), 4],
            [([1,2,5], 18), 5],
            [([1,2,5], 19), 5],
            [([1,2,5], 20), 4],]

    for x in input:
        a = coinChange(x[0][0], x[0][1])
        print("answer: ", a, " s/b: ", x[1], " Match: ", a == x[1])


if __name__=='__main__':
    main()
