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


'''
def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        All top and bottom rows will have single repeating pattern
        all mid rows will have two repeating patterns
        top/bottom row, every (numRows + 1)th
        mid rows, every () and (numRows + 1)th
        '''
        # Create list to store indexes in order:
        # every case will begin with s[0]
        indexes = [0]
        r = ""

        for i in range(numRows):
            # top row, every (numRows + 1)th:
            p = 0
            if (numRows + 1) < len(s):
                p += (numRows + 1)
            while p < (len(s)):
                indexes.append(p)
                p += (numRows + 1)

        for i in indexes:
            r = r + s[i]
        return r

def main() -> None:
    test = [("PAYPALISHIRING",3,"PAHNAPLSIIGYIR")]

    for i in test:
        a = convert(i[0],i[1])
        print("s/b: ", i[2], ", is: ", a)

if __name__=='__main__':
    main()
