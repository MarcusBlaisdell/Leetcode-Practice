'''
Leetcode 14
Longest Common Prefix

Write a function to find the longest common prefix string amongst
an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is
    non-empty.

Runtime beats 47.25%
Memory beats 26.90%
'''
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        r = ""

        for j in range(len(strs[0])):
            comp = strs[0][j]
            for i in strs:
                if len(i) <= j:
                    return r
                if i[j] != comp:
                    return r
            r += comp

        return r

def main() -> None:
    test = [(["flower","flow","flight"],"fl"),
            (["dog","racecar","car"],"")]

    for i in test:
        a = longestCommonPrefix(i[0])
        print("s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
