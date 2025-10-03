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

Passes 128/128
Runtime beats 5.01%
Memory beats 93.91%
'''
from typing import List
import time

def isAnagram(str1: str, str2: str):
    print("str1: ", str1, ", str2: ", str2)
    # First, check length:
    if len(str1) != len(str2):
        return False

    for i in str1:
        if str1.count(i) != str2.count(i):
            return False
    # Compare using dictionary
    dict1 = {}
    dict2 = {}

    for a in str1:
        if a in dict1:
            dict1[a] += 1
        else:
            dict1[a] = 1

    for a in str2:
        if a in dict2:
            dict2[a] += 1
        else:
            dict2[a] = 1

    #print("dict1: ", dict1)
    #print("dict2: ", dict2)

    for a in dict2.keys():
        if dict1[a]:
            if dict2[a] != dict1[a]:
                return False
        else:
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
            check for anagrams among remaining,
            remove elements as they are found
            and add to new list
            '''
            # seed the list:
            r.append([strs[0]])
            print("r, seeded: ", r)

            for i in range(1,len(strs)): # each element in input list
                found = 0
                print("strs[", i, "]: ", strs[i])
                print("r: ", r)
                for j in r: # each element in return list
                    print("j: ", j)
                    if isAnagram(strs[i], j[0]) == True:
                        print("append to current list")
                        j.append(strs[i])
                        found = 1
                        break
                if found == 0:
                    print("append to r")
                    r.append([strs[i]])
                else:
                    found = 0

        return r

def main() -> None:
    t1 = time.time()
    input = [(["eat","tea","tan","ate","nat","bat"],
            [["bat"],["nat","tan"],["ate","eat","tea"]]),
            ([""], [[""]]),
            (["a"],[["a"]]),
            (["ac","c"], [["ac"],["c"]])
            ]


    for i in input:
        a = groupAnagrams(i[0])
        print("s/b: ", i[1])
        print("is: ", a)

    print("total time: ", time.time() - t1)

    '''
    print("tea, eat: ", isAnagram("tea", "eat"))
    print("bat, cat: ", isAnagram("bat", "cat"))
    print("tatt, taat", isAnagram("tatt", "tat"))
    '''

if __name__=='__main__':
    main()
