'''
Leetcode 5
Longest Palindromic Substring

Given a string s, return the longest Palindromic Substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

'''

def longestPalindrome(s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        r = ""

        for c in range(len(s)):
            b = c
            l = len(s) - 1

            while(s[b] != s[l]):
                l -= 1
            f = b
            t = l

            if b == l:
                if len(r) <= 1:
                    r = s[b]
            else:
                while l > b:
                    #print("l: ", l, ", b: ", b)
                    while (s[b] == s[l]) and (((t+1) - f) > len(r)):
                        #print("b: ", b, ", l: ", l)
                        if (b == l) or (l < b):
                            if ((t+1) - f) >= len(r):
                                #print(s[f:t+1])
                                r = s[f:t+1]
                                break
                        if l == 0:
                            break
                        b += 1
                        l -= 1
                    if l > b:
                        if s[b] == s[l]:
                            l -= 1
                        else:
                            b = f
                            while(s[b] != s[l]):
                                l -= 1
                        t = l
        return r

def main() -> None:
    #test = [("aacabdkacaa", "aca")]

    test = [("babad","bab or aba"),
            ("cbbd","bb"),
            ("a", "a"),
            ("ac", "c"),
            ("bb", "bb"),
            ("ccc","ccc"),
            ("abb", "bb"),
            ("aacabdkacaa", "aca")]


    for i in test:
        a = longestPalindrome(i[0])
        print("s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
