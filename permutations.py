'''
Leetcode 46
Permutations
April 03, 2025
Given a list of integers, how many ways can they be arranged
e.g.
(1,2,3) can be expressed 6 ways as:
[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1)]
recursion?
'''
from typing import List

def helpPerm():
    # Solution, TBD:
    # base case, only one int in list:
    if len(s) == 1:
        return s[0]

    for i in s:
        newS = s
        temp = [i]
        newS.pop(i)
        helpPerm(newS)

def getPerm(s: List[int]) -> List[List[int]]:
    # store all possible solutions in a list
    a = []




    return a

def main() -> None:
    input = [[1,2,3]]

    for s in input:
        answer = getPerm(s)
        print("answer: ", answer)

if __name__=='__main__':
    main()
