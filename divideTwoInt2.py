'''
Leetcode 29
Divide Two Integers

Given two integers dividend and divisor, divide two integers
without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means
losing its fractional part. For example, 8.345 would be truncated
to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only
store integers within the 32-bit signed integer range:
[−2^31, 2^31 − 1]. For this problem, if the quotient is strictly
greater than 2^31 - 1, then return 2^31 - 1, and if the quotient
is strictly less than -2^31, then return -2^31.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.



Constraints:

    -2^31 <= dividend, divisor <= 2^31 - 1
    divisor != 0

994/994
Runtime beats 100%
Memory beats 13.96%
'''
import time

def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        # determine sign:
        sign = 1

        if dividend < 0 and divisor < 0:
            sign = 1
        if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0):
            sign = -1

        # force both positive:
        dividend = abs(dividend)
        divisor = abs(divisor)
        dr = divisor

        if divisor == 1:
            ans = dividend
        else:
            while dividend >= divisor:
                ansT = 0
                if (dividend - dr) < dr:
                    ans += 1
                    dividend = dividend - dr
                else:
                    while dr <= dividend:
                        if (dr + dr) <= dividend:
                            dr = dr + dr
                            if ansT == 0:
                                ansT += 2
                            else:
                                ansT += ansT
                        else:
                            break

                    ans += ansT

                    if ans > 0:
                        dividend = dividend - dr
                    dr = divisor

        ans = ans * sign

        if ans > ((2**31) - 1):
            ans = ((2**31) - 1)
        if ans <= -2**31:
            ans = -2**31
        return ans

def main() -> None:
    t1 = time.time()

    #test = [[-2147483648, 2, -1073741824]]

    '''
    test = [[10, 3, 3],
            [7, -3, -2],
            [1, 1, 1],
            [-2147483648, -1, 2147483647]]

    '''
    test = [[10, 3, 3],
            [7, -3, -2],
            [1, 1, 1],
            [-2147483648, -1, 2147483647],
            [-2147483648, 1, -2147483648],
            [2147483647, 2, 1073741823],
            [2147483647, 3, 715827882],
            [-2147483648, 2, -1073741824]]

    for i in test:
        a = divide(i[0], i[1])
        print("s/b: ", i[2], ", is: ", a, i[2] == a)

    print("total time: ", time.time() - t1)

if __name__=='__main__':
    main()
