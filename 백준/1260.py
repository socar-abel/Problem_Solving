from collections import deque

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b) 
    graph[b].append(a)

for x in graph:
    x.sort()

visited = [False]*(N+1)
visited2 = [False]*(N+1)

def dfs(node):
    print(node,end = ' ')
    visited[node] = True
    for x in graph[node]:
        if not visited[x]: dfs(x)

def bfs(node):
    q = deque()
    q.append(node)
    visited2[node] = True
    print(node,end = ' ')

    while q:
        now = q.popleft() 
        
        for x in graph[now]:
            if not visited2[x]: 
                print(x,end= ' ')
                q.append(x)
                visited2[x] = True

dfs(V)
print()
bfs(V)
