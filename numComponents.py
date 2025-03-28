'''
LeetCode 323
Number of Connected Components in an Undirected Graph
UnionFind algorithm
May 28, 2025
'''

n = 5

par = [i for i in range(n)]
rank = [1] * n

def find(e1):
    while e1 != par[e1]:
        par[e1] = par[par[e1]]
        e1 = par[e1]
    return e1

def union(e1, e2):
    p1, p2 = find(e1), find(e2)

    if p1 == p2:
        return 0

    if rank[p2] > rank [p1]:
        par[p1] = p2
        rank[p2] += rank[p1]
    else:
        par[p2] = p1
        rank[p1] += rank[p2]
    return 1

def main():
    edges = [[0,1], [1,2], [3,4]]

    count = n

    for e1, e2 in edges:
        val = union(e1, e2)
        count -= val

    print("Count: ", count)

if __name__=='__main__':
    main()
