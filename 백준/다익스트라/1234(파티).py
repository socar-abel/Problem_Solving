import sys
import heapq
N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
INF = 987654321

for _ in range(M):
    A, B, T = map(int, sys.stdin.readline().split())
    graph[A].append((B, T))


def dijkstra(start, end):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for node, d in graph[now]:
            cost = dist + d
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

    return distance[end]


answer = 0
for i in range(1, N+1):
    go = dijkstra(i, X)
    back = dijkstra(X, i)
    result = go + back
    answer = max(answer, result)

print(answer)
