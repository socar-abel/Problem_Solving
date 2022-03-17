from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)
semester = [1] * (N+1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    inDegree[B] += 1

q = deque()
for x in range(1, N+1):
    if inDegree[x] == 0:
        q.append((x, 1))

while q:
    now, sem = q.popleft()

    for node in graph[now]:
        inDegree[node] -= 1
        if inDegree[node] == 0:
            semester[node] = sem + 1
            q.append((node, sem + 1))

for s in semester[1:]:
    print(s, end=' ')

