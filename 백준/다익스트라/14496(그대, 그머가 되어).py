import sys
import heapq
INF = 987654321

A, B = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    # (노드, 거리)
    graph[x].append((y, 1))
    graph[y].append((x, 1))


# 다익스트라
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(A)
answer = distance[B]
if answer == INF:
    print(-1)
else:
    print(answer)
