import sys
import heapq

INF = 987654321

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distance = [INF] * (N + 1)


def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue  # 방문처리

        for x in graph[now]:
            cost = dist + 1
            if distance[x] > cost:
                distance[x] = cost
                heapq.heappush(q, (cost, x))


dijkstra(X)

check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if not check:
    print(-1)
