'''
Leetcode 17
Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number
could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone
buttons) is given below. Note that 1 does not map to any letters.

1      2abc  3def
4ghi   5jkl  6mno
7pqrs  8tuv  9wxyz
*+     0_    #^

2, abc
3, def
4, ghi
5, jkl
6, mno
7, pqrs
8, tuv
9, wxyz

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]



Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].


digitDict = {'2': ['a', 'b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']}

Graph with dynamic programming

Runtime beats 100%
Memory beats 11.91%
'''
from typing import List
import time

def letterCombinations(digits: str) -> List:
        """
        :type digits: str
        :rtype: List[str]
        """
        r = []
        # if there are no digits, return empty list:
        if len(digits) == 0:
            return []

        digitList = [[], [], ['a', 'b','c'],
                    ['d','e','f'],
                    ['g','h','i'],
                    ['j','k','l'],
                    ['m','n','o'],
                    ['p','q','r','s'],
                    ['t','u','v'],
                    ['w','x','y','z']]

        if len(digits) == 1:
            return digitList[int(digits[0])]

        # If we get here, we have at least 2 digits:
        # start with last digit
        for i in range(len(digits) - 1, -1, -1):
            temp = []
            if len(r) > 0:
                for j in digitList[int(digits[i])]:
                    for k in r:
                        temp.append(j + k)
                r = temp
            else:
                for j in digitList[int(digits[i])]:
                    r.append(j)

        return r

def main() -> None:
    t1 = time.time()
    test = [("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
            ("", []),
            ("2", ["a","b","c"]),
            ("234", ["tbd"])]

    for i in test:
        a = letterCombinations(i[0])
        print("s/b: ", i[1], ", is: ", a)

    print("Total time: ", t1 - time.time())

if __name__=='__main__':
    main()
