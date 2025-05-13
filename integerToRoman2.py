'''
Leetcode 12
Integer to Roman

Lookup method

I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Runtime beats 100%
memory beats 13.34%
'''
def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        r = ""

        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        x = num // 1000
        r += thousands[x]

        num = num % 1000
        x = num // 100
        r += hundreds[x]

        num = num % 100
        x = num // 10
        r += tens[x]

        num = num % 10
        x = num
        r += ones[x]

        return r


def main() -> None:
    test = [(3749, "MMMDCCXLIX"),
            (58,"LVIII"),
            (1994, "MCMXCIV"),
            (3999, "MMMCMXCIX"),
            (10,"X"),
            (100, "C"),
            (1000, "M")]

    for i in test:
        a = intToRoman(i[0])
        print(i[0], ", s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
