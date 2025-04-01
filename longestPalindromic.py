'''
Leetcode 5
Longest Palindromic substring
April 01, 2025
'''

# Function to find longest palindromic substring
# from a given string
# Accepts a string, returns a string
def longestPalindrome(s: str) -> str:
    # create a blank string, solution, to store the result,
    # and a size variable, size, to track length to know
    # if we found something bigger:
    solution = ""
    size = 0

    # loop through each character in the string:
    for i in range(len(s)):
        '''
        initialize index pointers to current character:
        2 posibilities:
        1) the string is odd sized
        2) the string is even sized
        This necessitates running it twice to catch all possibilities, 
        once for odd case, and again for even case
        '''
        # Odd sized:
        i1, i2 = i, i

        while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
            curSize = i2 - i1 + 1
            if (curSize) > size:
                solution = s[i1:i2+1]
                size = curSize
            i1 -= 1
            i2 += 1

        # Even sized:
        if i1 < len(s) - 2:
            i1, i2 = i, i + 1
        while ((i1 >= 0) and (i2 < len(s))) and (s[i1] == s[i2]):
            curSize = i2 - i1 + 1
            if (curSize) > size:
                solution = s[i1:i2+1]
                size = curSize
            i1 -= 1
            i2 += 1
    return solution

def main() -> None:
    testStrings = [("babad", "bab or aba"),
                    ("cbbd", "bb"),
                    ("abccabbacdef", "cabbac"),
                    ("abccabacdef", "cabac"),
                    ("abccabbbacdef", "cabbbac"),
                    ("abccabbbbacdef", "cabbbbac")]

    for s, a in testStrings:
        answer = longestPalindrome(s)
        print("answer: ", answer)
        print("s/b: ", a)

if __name__=='__main__':
    main()
