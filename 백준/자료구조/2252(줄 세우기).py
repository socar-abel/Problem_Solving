import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)
answer = []
h = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    inDegree[B] += 1

for i in range(1, N+1):
    if inDegree[i] == 0:
        heapq.heappush(h, i)

while h:
    now = heapq.heappop(h)
    answer.append(now)
    for x in graph[now]:
        inDegree[x] -= 1
        if inDegree[x] == 0:
            heapq.heappush(h, x)

for a in answer:
    print(a, end=' ')
