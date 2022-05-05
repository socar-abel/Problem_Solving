from collections import deque
import sys
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
leaves = []
depth = dict()

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append((1, 0)) # 노드, 깊이
visit[1] = True

while q:
    now, d = q.popleft()

    isLeaf = True
    for x in graph[now]:
        if not visit[x]:
            isLeaf = False
            q.append((x, d + 1))
            visit[x] = True

    if isLeaf:
        depth[now] = d

total = 0
for key in depth:
    total += depth[key]

if total % 2 == 0:
    print("No")
else:
    print("Yes")

