'''
Leetcode 49
Group Anagrams
Medium

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be
    rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be
    rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

'''
from typing import List
import time

def isAnagram(str1: str, str2: str) -> Bool:
    for i in str1:
        if str1.count(i) != str2.count(i):
            return False
    return True

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        r = []

        if len(strs) == 1:
            r.append(strs)
        else:
            '''
            while there are elements in the list,
            remove first element and add to new list
            check for anagagrams among remaining,
            remove elements as they are found
            and add to new list
            '''

        return r

def main() -> None:
    t1 = time.time()
    input = [(["eat","tea","tan","ate","nat","bat"],
            [["bat"],["nat","tan"],["ate","eat","tea"]]),
            ([""], [[""]]),
            (["a"],[["a"]])
            ]

    for i in input:
        a = groupAnagrams(i[0])
        print("s/b: ", i[1])
        print("is: ", a)

    print("total time: ", time.time() - t1)


if __name__=='__main__':
    main()
