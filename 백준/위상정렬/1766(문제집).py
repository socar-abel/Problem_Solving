import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
inDegree = [0]*(N+1)
answer = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    inDegree[B] += 1

h = []
for i in range(1, N+1):
    if inDegree[i] == 0:
        heapq.heappush(h, i)

while h:
    now = heapq.heappop(h)
    answer.append(now)
    for neighbor in graph[now]:
        inDegree[neighbor] -= 1
        if inDegree[neighbor] == 0:
            heapq.heappush(h, neighbor)

for x in answer:
    print(x, end=' ')
