import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [-1] * (N+1)

def dfs(node, p):
    visit[node] = True
    parent[node] = p

    for x in graph[node]:
        if not visit[x]:
            dfs(x, node)

dfs(1,0)
for i in range(2, N+1):
    print(parent[i])
