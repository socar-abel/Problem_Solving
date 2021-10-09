import heapq
import sys
INF = 987654321

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
d = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start):
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue

        for x in graph[now]:
            cost = dist + x[1]

            if cost < d[x[0]]:
                d[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))


s, t = map(int, sys.stdin.readline().split())
dijkstra(s)
print(d[t])
