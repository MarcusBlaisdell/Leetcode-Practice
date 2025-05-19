'''
Leetcode 15
Three Sum
   return all sets of three numbers that sum to zero
May 31, 2025
-1, 0, 1, 2, -1, -4
-4, -1, -1, 0, 1, 2

Solution exceeds time limit on Leetcode
'''

def twoSum(theArray, n, i1):
    i2 = len(theArray) - 1
    while(i1 < i2):
        if (n + theArray[i1] + theArray[i2]) == 0:
            return i1, i2
        elif (n + theArray[i1] + theArray[i2]) > 0:
            i2 -= 1
        elif (n + theArray[i1] + theArray[i2]) < 0:
            i1 += 1
    return i1, i2

def threeSum(theArray):
    theArray.sort()
    solutionSet = []
    i1 = 1
    i2 = len(theArray) - 1

    for i, n in enumerate(theArray):
        i1 = i + 1
        # find all possible solutions:
        while i1 < i2:
            i1, i2 = twoSum(theArray, n, i1)
            if (i1 != i2):
                s1 = theArray[i1]
                s2 = theArray[i2]
                if ((n,s1,s2) not in solutionSet):
                    solutionSet.append((n,s1,s2))
            i1 += 1

    print("Solution set: ", solutionSet)

def main():
    theArray = [-1,0,1,2,-1,-4]
    #theArray = [-3, 3, 4, -3, 1, 2, -4]
    threeSum(theArray)


if __name__=='__main__':
    main()
