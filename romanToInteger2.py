'''
Leetcode 13
Roman to Integer

Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.

Symbol       Value
I", 1
V", 5
X", 10
L", 50
C", 100
D", 500
M", 1000

Runtime beats 86.37%
Memory beats 53.91%

Definitely an improvement, but there seems to still be a better
way.
'''
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        r = 0

        rDict = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}

        for c in range(len(s)):
            r += rDict[s[c]]
            if c > 0:
                if rDict[s[c]] > rDict[s[c-1]]:
                    r -= (2 * rDict[s[c-1]])

        return r

def main() -> None:
    test = [("III", 3),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
            ("MMMDCCXLIX", 3749),
            ("MMMDCCXL", 3740),
            ("MMMCCXLIX", 3249),
            ("DCXXI",621),
            ("MCDLXXVI",1476),
            ("MMCCCX",2310),
            ("MDCXCV",1695),
            ("CXC",190),
            ("MMMXL",3040),
            ("MMMCML",3950),
            ("MCM",1900)]

    for i in test:
        a = romanToInt(i[0])
        print(i[0], ", s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
