from itertools import combinations
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

def dfs(node, comb):
    comb.append(node)
    if len(comb) == M:
        for x in comb:
            print(x, end=' ')
        print()
        return

    for i in range(node+1, N+1):
        dfs(i, comb)
        comb.pop()

for i in range(1, N+1):
    dfs(i, [])


