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
    dp = [False] * (len(i) + 1)
    dp[len(i)] = True

    for x in range(len(i) -1, -1, -1):
        for w in d:
            if ((x + len(w)) <= len(i)) and i[x:(x + len(w))] == w:
                dp[x] = dp[x + len(w)]
            if dp[x]:
                break

    return dp[0]

def main() -> None:
    test =  [
            ["leetcode",["leet","code"]],
            ["codebase",["base","code"]],
            ["codebase",["base","cod"]]
            ]

    for i in test:
        answer = wordBreak(i[0], i[1])
        print(i[0], "- Answer: ", answer)

if __name__=='__main__':
    main()
