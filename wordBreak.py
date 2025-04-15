'''
Leetcode 139
Word break

Given a string s and a dictionary of strings wordDict, return true
if s can be segmented into a space-separated sequence of one or more
dictionary words.
The same word in the dictionary may be reused multiple times in the
segmentation.

Example 1:
Input: s = "leetcode"
wordDict = ["leet", "code"]
Output: true
'''
from typing import List

def wordBreak(i: str, d: List) -> bool:
    y = 0
    for l in d[1]:
        if l != i[y]:
            return False
        y += 1

    return True

def main() -> None:
    input = "leetcode"
    wordDict = ["leet", "code"]

    answer = wordBreak(input, wordDict)
    print("Answer: ", answer)

if __name__=='__main__':
    main()
