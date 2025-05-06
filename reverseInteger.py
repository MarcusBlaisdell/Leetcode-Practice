'''
Leetcode 7
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21



Constraints:

    -2^31 <= x <= 2^31 - 1

Beats: 89.36%
'''
def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        n = 1
        c = 0

        if x < 0:
            n = -1
            x *= -1

        while x > 0:
            r *= 10
            r += (x % 10)
            if (r > 2147483648):
                return 0
            x = x // 10
            c += 1

        return r * n

def main() -> None:
    test = [(123, 321),
            (-123, -321),
            (120, 21),
            (1534236469, 0),
            (-2147483412, -2143847412)]

    for i in test:
        a = reverse(i[0])
        print("s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
