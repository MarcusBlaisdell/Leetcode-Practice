'''
Leetcode 9
Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



Constraints:

    -2^31 <= x <= 2^31 - 1


Follow up: Could you solve it without converting the integer to a string?

Runtime beats 95.16%
memory beats 51.72%
'''
def isPalindrome(x: int) -> bool:
    """
    :type x: int
    :rtype: bool
    """
    # a negative cannot be a palindrome because
    # -121 != 121-
    if x < 0:
        return False

    # it must be positive, reverse the digits, and check if equal:
    r = False
    y = 0
    z = x

    while z > 0:
        i = (z % 10)
        y *= 10
        y += i
        z = z // 10

    if x == y:
        return True

    return r

def main() -> None:
    test = [(121,True),
            (-121,False),
            (10,False),
            (5445,True)]

    for i in test:
        a = isPalindrome(i[0])
        print("s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
