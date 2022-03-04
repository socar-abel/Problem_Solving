from collections import deque
import sys
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)
cost = [0] * (N+1)
inDegree = [0] * (N+1)

for i in range(1, N+1):
    inputList = list(map(int, sys.stdin.readline().split()))
    time[i] = inputList[0]
    for x in inputList[1:]:
        if x == -1:
            break
        graph[x].append(i)
        inDegree[i] += 1

startNodes = []
for i in range(1, N+1):
    if inDegree[i] == 0:
        startNodes.append(i)

q = deque()
for x in startNodes:
    cost[x] = time[x]
    q.append((x, time[x]))

while q:
    now, t = q.popleft()
    for x in graph[now]:
        inDegree[x] -= 1
        cost[x] = max(cost[x], time[x] + t)
        if inDegree[x] == 0:
            q.append((x, cost[x]))

for c in cost[1:]:
    print(c)
