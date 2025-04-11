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

Dependencies are provided in a list, use a list to track?
numCourses = 5
Dependencies:
0: 1, 2
1: 3, 4
2: None
3: 4
4: None
Reachable:
0: 1 and 2 are reachable so yes
1: 3 and 4 are reachable so yes
2: Yes
3: 4 is reachable so yes
4: Yes

Read through prerequisites list, populate Dependencies list
'''
from typing import List

def finishHelp(d: List[List[int]], v: List[int], c: int) -> bool:
    if c in v:
        return False

    v.append(c)
    #base case, list is empty, course is reachable:
    if not d[c]:
        return True
    else:
        # given course c, check if it's reachable:
        # Check all prerequisites for the course:
        for i in d[c]:
            a = finishHelp(d, v, d[c][0])

            if a:
                d[c].remove(d[c][0])
                return True
            else:
                return False

    # What does not possible look like?

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Create lists of dependencies:
    dependencies = []
    for i in range(numCourses):
        dependencies.append([])

    # Populate dependencies list:
    for i in prerequisites:
        dependencies[i[0]].append(i[1])

    # Check each course to see if it can be completed:
    for i in range(numCourses):
        visited = []
        val = finishHelp(dependencies, visited, i)
        if val == False:
            return False

    return True

def main() -> None:
    testData = [(2,[[1,0]]),
                (5,[[0,1], [0,2], [1,3], [1,4], [3,4]]),
                (5, [[0,1], [1,0], [1,3], [1,4], [3,4]])]

    for i in testData:
        answer = canFinish(i[0], i[1])
        print("answer: ", answer)

if __name__=='__main__':
    main()
