'''
Leetcode 13
Roman to Integer

Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones
added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to
right. However, the numeral for four is not IIII. Instead, the number
four is written as IV. Because the one is before the five we subtract
it making four. The same principle applies to the number nine, which is
written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range
    [1, 3999].

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

'''
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        i = 0

        # handle 1000's:
        if s[0] == 'M':
            while s[i] == 'M':
                r += 1000
                i += 1

        if s[i] == 'C' and s[i+1] == 'M':
            r += 900
            i += 2

        # 100's
        if s[i] == 'D':
            r += 500
            i += 1
        if s[i] == 'C':
            while s[i] == 'C':
                r += 100
                i += 1

        # 10's
        if s[i] == 'X' and s[i+1] == 'C':
            r += 90
            i += 2
        if s[i] == 'X' and s[i+1] == 'L':
            r += 40
            i += 2
        if s[i] == 'L':
            r += 50
            i += 1
        if s[i] == 'X':
            while s[i] == 'X':
                r += 10
                i += 1

        while i < len(s):
            # 1's
            if s[i] == 'V':
                r += 5
                i += 1
            if s[i] == 'I':
                if i <= len(s) - 2:
                    if s[i+1] == 'X':
                        r += 9
                        i += 2
                    if s[i+1] == 'V':
                        r += 4
                        i += 2
                if i < len(s):
                    while s[i] == 'I' and i < len(s):
                        r += 1
                        i += 1

        return r

def main() -> None:
    test = [("III", 3),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
            ("MMMDCCXLIX", 3749),
            ("MMMCCXLIX", 3249)]

    for i in test:
        a = romanToInt(i[0])
        print(i[0], ", s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
