'''
Leetcode 12
Integer to Roman

Seven different symbols represent Roman numerals with the following values:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values
from highest to lowest. Converting a decimal place value into a Roman numeral
has the following rules:

    If the value does not start with 4 or 9, select the symbol of the manumimal
    value that can be subtracted from the input, append that symbol to the
    result, subtract its value, and convert the remainder to a Roman numeral.
    If the value starts with 4 or 9 use the subtractive form representing one
    symbol subtracted from the following symbol, for enumample, 4 is 1 (I) less
    than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following
    subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and
    900 (CM).
    Only powers of 10 (I, X, C, M) can be appended consecutively at most 3
    times to represent multiples of 10. You cannot append 5 (V), 50 (L), or
    500 (D) multiple times. If you need to append a symbol 4 times use the
    subtractive form.

Given an integer, convert it to a Roman numeral.



Enumample 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Enumplanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on
decimal places

Enumample 2:

Input: num = 58

Output: "LVIII"

Enumplanation:

50 = L
 8 = VIII

Enumample 3:

Input: num = 1994

Output: "MCMXCIV"

Enumplanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV



Constraints:

    1 <= num <= 3999

I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Beats Runtime: 62.09%
Beats memory: 13.34%
'''
def intToRoman(num: int) -> str:
    """
    :type num: int
    :rtype: str
    """
    r = ''
    '''
    handle 1000's:
    constraint, num will never enumceed 3,999,
    so just add as many 'M's as needed:
    '''
    if num > 1000:
    	y = num // 1000
    	for i in range(y):
        	r += 'M'
    	num = num % 1000

    '''
    Handle 100's:
    for each value over 100 up to 300:
    	add 'C',
    if 400:
    	add 'CD'
    if > 500 and < 900:
    	add 'D' + 'C'
    if => 900:
    	add 'CM'
    '''
    if num >= 900:
    	r += 'CM'
    	num = num % 100
    if num >= 500:
    	r += 'D'
    	num -= 500
    	y = num // 100
    	for i in range(y):
        	r += 'C'
    	num = num % 100
    if num >= 400:
    	r += 'CD'
    if num < 400:
    	y = num // 100
    	for i in range(y):
        	r += 'C'
    num = num % 100

    '''
    Handle 10's:

    '''
    if num >= 90:
    	r += 'XC'
    	num = num % 10
    if num >= 50:
    	r += 'L'
    	y = (num - 50) // 10
    	for i in range(y):
        	r += 'X'
    	num = num % 10
    if num >= 40:
    	r += 'XL'
    	num = num % 10
    if num > 10:
    	y = num // 10
    	for i in range(y):
        	r += 'X'
    	num = num % 10

    '''
    Handle 1's:
    '''
    if num == 10:
        r += 'X'
        return r
    if num == 9:
    	r += 'IX'
    	return r
    if num >= 5:
    	r += 'V'
    	y = num - 5
    	for i in range(y):
        	r += 'I'
    	return r
    if num == 4:
    	r += 'IV'
    	return r
    for i in range(num):
    	r += 'I'

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
        print("s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
