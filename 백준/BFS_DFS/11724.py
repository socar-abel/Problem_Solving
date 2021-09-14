# input() 말고 sys.stdin.readline() 써야 시간복잡도 통과함 !

import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    for x in graph[node]:
        if not visited[x]:
            dfs(x)

count = 0
for x in range(1,N+1):
    if not visited[x]: dfs(x); count += 1

print(count)
