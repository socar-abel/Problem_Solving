import sys
import heapq
INF = 987654321
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    # 출발 노드, 도착 노드, 비용
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start, end):
    # [거리, 지나온 경로]
    distance = [[INF, []] for _ in range(N + 1)]
    distance[start] = [0, [start]]

    q = []
    # (거리, 노드, 지나온 경로)
    heapq.heappush(q, (0, start, [start]))

    while q:
        dist, now, path = heapq.heappop(q)
        if distance[now][0] < dist:
            continue

        for node, d in graph[now]:
            cost = dist + d

            if cost < distance[node][0]:
                distance[node][0] = cost
                distance[node][1] = path + [node]
                q.append((cost, node, path + [node]))

    print(distance[end][0])
    print(len(distance[end][1]))
    for x in distance[end][1]:
        print(x, end=' ')


S, E = map(int, sys.stdin.readline().split())
dijkstra(S, E)

