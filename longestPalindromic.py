'''
Leetcode 5
Longest Palindromic substring
April 01, 2025
'''

def longestPalindrome(s: str) -> str:
    solution = ""
    size = 0

    for i in range(len(s)):
        i1, i2 = i, i
        if (i < len(s) - 1) and (s[i1] == s[i2+1]):
            i2 += 1
        while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
            curSize = i2 - i1 + 1
            if (curSize) > size:
                solution = s[i1:i2+1]
                size = curSize
            i1 -= 1
            i2 += 1
    return solution

def main() -> None:
    #s = "babad" # bab or aba
    #s = "cbbd" # bb
    #s = "abccabbacdef" # cabbac
    s = "abccabacdef" # cabac

    result = longestPalindrome(s)
    print("Result: ", result)

if __name__=='__main__':
    main()
