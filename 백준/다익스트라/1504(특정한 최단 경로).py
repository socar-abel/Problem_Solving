import heapq
import sys

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
INF = 987654321

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

V1, V2 = map(int, sys.stdin.readline().split())


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


case1 = dijkstra(1, V1) + dijkstra(V1, V2) + dijkstra(V2, N)
case2 = dijkstra(1, V2) + dijkstra(V2, V1) + dijkstra(V1, N)
answer = min(case1, case2)

if answer < INF:
    print(answer)
else:
    print(-1)
