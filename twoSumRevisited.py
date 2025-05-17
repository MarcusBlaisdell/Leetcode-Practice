'''
Two Sum revisited
'''
from typing import List

def twoSum(nums: List) -> List:
    r = []

    for i in nums:
        nums2 = nums
        nums2.remove(i)
        if (0 - i) in nums2:
            add = [i, 0 - i]
            add.sort()
            if (add) not in r:
                r.append(add)

    return r


def main()-> None:
    test = [([-1,0,1,2,-1,-4], [[-1,1]]),
            ([0,1,1], []),
            ([0,0,0], [[0,0]]),
            ([1,2,-3],[]),
            ([-1, 1, 0, -2, 2, -3, 3],[[-1,1],[-2,2],[-3,3]])]

    for i in test:
        a = twoSum(i[0])
        print("s/b: ", i[1], ", is: ", a)

if __name__=='__main__':
    main()
