'''
Leetcode 207
Course Schedule
April 10, 2025
There are a total of numCourses you must take, labeled
from 0 to numCourses-1.
Some courses have prerequisites.
E.G. to take course 0, you must first take course 1,
expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs,
is it possible to finish all courses

Some type of tree?

E.G. 2 course, [1,0], must take course 0 to take course 1
Can take course 0, then course 1 for 2 classes total
   0
  /
 1
E.G.
numCourses = 5,
prerequisites = [[0,1], [0,2], [1,3], [1,4], [3,4]]
      0
     / \
    1   2
   / \
  3   4
 /
4
'''
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    possible = False
    # Do stuff
    return possible

def main() -> None:
    testData = [(2,[[1,0]])]

    for i in testData:
        answer = canFinish(i[0], i[1])
        print("answer: ", answer)

if __name__=='__main__':
    main()
