'''
Leetcode 3
Longest substring w/o repeating characters
April 02, 2025
Use set to track characters we've encountered
a
a, b
a, b, c
a, b, c, a: a is already in, if len(a) > maxlen, maxlen = len(a)
move pointer until a is encountered, remove characters from set
until duplicate is found, increment index by 1
'''

def longestSub(s: str) -> int:
    a = set()
    maxlen = 0
    i = 0 # index of last repeated character

    # check each character, one-by-one:
    for c in range(len(s)):
        # if we found a duplicated character,
        # handle it:
        if s[c] in a:
            if len(a) > maxlen:
                maxlen = len(a)
            # find the index of the repeated character
            while s[i] != s[c]:
                a.remove(s[i])
                i += 1
            i += 1
            a.add(s[c])
        else:
            a.add(s[c])
    # if no character was repeated through the end
    # of the string, check the length again:
    if len(a) > maxlen:
        maxlen = len(a)

    return maxlen

def main() -> None:
    sList = [("abcabcbb", 3),
            ("abccdefghijj", 8),
            ("abcdefbghi", 8),
            ("cdefbghi", 8),
            ("abcdefbgahcid", 9),
            ("abcdefabcd", 6),
            ("jbpnbwwd",4),
            ("dvdf", 3)]
    '''

    sList = [("jbpnbwwd",4),
            ("dvdf", 3)]
    '''

    for s, a in sList:
        answer = longestSub(s)
        print("Answer: ", answer, " s/b: ", a)

if __name__=='__main__':
    main()
