'''
Leetcode 6
Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

PAYPALISHIRING
PAHNAPLSIIGYIR
0,4,8,12, 1,3,5,7,9,11,13, 2,6,10,(14)

Write the code that will take a string and make this conversion given a
number of rows:

string convert(string s, int numRows);



Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I     N
A   L S   I G
Y A   H R
P     I

PAYPALISHIRING
PINALSIGYAHRPI
0,6,12, 1,5,7,11,13, 2,4,8,10, 3, 9

Example 3:

Input: s = "A", numRows = 1
Output: "A"



Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

Achieves 15% on Leetcode
'''
import time

def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        a = ""

        for i in range(numRows):
            for j in range(i, len(s), 2 * (numRows - 1)):
                a += s[j]
                if (i > 0 and i < numRows - 1 and j + 2 * (numRows - 1) - 2 * i < len(s)):
                    a += s[j + 2 * (numRows - 1) - 2 * i]
        return a

def main() -> None:
    test = [("PAYPALISHIRING",3,"PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING",4,"PINALSIGYAHRPI")]

    t = time.time()

    for i in test:
        a = convert(i[0],i[1])
        print(" s/b: ", i[2])
        print(", is: ", a)
        print("")
        for x in range(len(i[0])):
            if i[2][x] != a[x]:
                print("mismatch, x: ", x, ", i[2][x]: ", i[2][x], ", a[x]: ", a[x])
                break

    print("Total time: ", time.time() - t)


if __name__=='__main__':
    main()
