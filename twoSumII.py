'''
Leetcode 167
Two sum II, array is sorted
Hash map
<Month>, <Day>, <Year>
'''

def findIndexes(theArray, target):
    index1 = 0
    index2 = len(theArray) - 1

    while(index1 < index2):

        if (theArray[index1] + theArray[index2]) == target:
            return index1, index2

        elif (theArray[index1] + theArray[index2]) > target:
            index2 -= 1

        elif (theArray[index1] + theArray[index2]) < target:
            index1 += 1

    return -1, -1



def main():
    '''
    theArray = [2,7,11,15]
    target = 9
    '''
    theArray = [1,3,4,5,7,10,11]
    target = 9
    

    index1, index2 = findIndexes(theArray, target)

    print("Solution: ", index1, ", ", index2)

if __name__=='__main__':
    main()
