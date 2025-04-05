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

def getPerm(s: List[int]) -> List[List[int]]:
    # create a list to store results:
    a = []

    # base case:
    if len(s) == 1:
        # not working to just return s,
        # it does work if I use slicing and specify
        # the whole range
        return [s[0:]]

    # otherwise, for each character, remove it from the list,
    # and pass the remainder to the recursive call:
    for i in range(len(s)):
        c = s.pop(0)
        p = getPerm(s)

        # build the list from the returns from the
        # recursive calls:
        for x in p:
            x.append(c)
        a.extend(p)
        s.append(c)

    return a

def main() -> None:
    input = [[1,2,3]]

    for s in input:
        answer = getPerm(s)
        print("answer: ", answer)

if __name__=='__main__':
    main()
