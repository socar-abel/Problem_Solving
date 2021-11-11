from collections import deque
import sys
n = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

find = False
q = deque()
q.append((A,0))
visit[A] = True

while q:
    now, num = q.popleft()

    for node in graph[now]:
        if not visit[node]:
            q.append((node, num+1))
            visit[node] = True
            if node == B:
                find = True
                print(num+1)
                break

if not find:
    print(-1)

