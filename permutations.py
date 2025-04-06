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
        '''
        not working to just return s, or s[0]
        it does work if I use slicing and specify
        the whole range
        Testing on console:
        Create a list with just one int:
        >>> intLista = [1]
        View it:
        >>> intLista
        [1]
        print as is, as part of a list:
        >>> print([intLista])
        [[1]]
        compare with using slicing:
        >>> print([intLista[0:]])
        [[1]]
        output is the same, so why can't I use [intLista]
        and have to use [intLista[0:]]?
        also works with:
        [s[0:len(s)]]
        Works with:
        [[s[0]]]
        Makes it a List[List[int]]
        '''
        #return [s[0:]] # This works
        return [[s[0]]] # making it a List of a List also works
        #return [[s]] # does not work

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
    input = [[1,2,3], [1,2,3,4]]

    for s in input:
        answer = getPerm(s)
        print("answer: ", answer)

if __name__=='__main__':
    main()
