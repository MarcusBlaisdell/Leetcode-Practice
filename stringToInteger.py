'''
Leetcode 8
String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string
to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    1. Whitespace: Ignore any leading whitespace (" ").
    2. Signedness: Determine the sign by checking if the next character
       is '-' or '+', assuming positivity if neither present.
    3. Conversion: Read the integer by skipping leading zeros until a
       non-digit character is encountered or the end of the string is
       reached. If no digits were read, then the result is 0.
    4. Rounding: If the integer is out of the 32-bit signed integer
       range [-2^31, 2^31 - 1], then round the integer to remain in the
       range. Specifically, integers less than -2^31 should be rounded to
       -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.

Return the integer as the final result.



Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the
current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^

Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^

Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character
        is a non-digit)
             ^

Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a
        non-digit)
          ^

Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.



Constraints:

    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case),
    digits (0-9), ' ', '+', '-', and '.'.

Runtime beats 100%
memory beats 15.49%
'''
def myAtoi(s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        cdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9}
        sign = 1
        i = 0

        while i < len(s):
            if s[i] == '-':
                sign = -1
                i += 1
                break
            elif (s[i] == '+'):
                i += 1
                break
            elif (s[i] == ' '):
                i += 1
            elif (s[i] not in '0123456789'):
                break
            elif s[i] in '0123456789':
                break

        while i < len(s):
            if s[i] not in '0123456789':
                break
            else:
                r *= 10
                r += cdict[s[i]]
            i += 1

        r = r * sign
        print("r: ", r)

        if r < -2**31:
            return -2**31
        if r >= 2**31:
            return (2**31) - 1

        return r

def main() -> None:
    test = [("42", 42),
            ("-042", -42),
            ("1337c0d3", 1337),
            ("0-1", 0),
            ("words and 987", 0),
            ("   -042", -42),
            ("-91283472332",-2147483648),
            ("91283472332",2147483647),
            ("      -11919730356x",-2147483648),
            ("      11919730356x",2147483647)]

    for i in test:
        a = myAtoi(i[0])
        print("s/b: ", i[1], ", is: ", a)
    print("-11919730356 < -2**31: ", -11919730356 < -2**31)

if __name__=='__main__':
    main()
