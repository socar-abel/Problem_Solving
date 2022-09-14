import sys
import heapq
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = 1e9


def dijkstra(n, graph):
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (0, 0, graph[0][0]))

    while q:
        x, y, dist = heapq.heappop(q)
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    heapq.heappush(q, (nx, ny, cost))
                    distance[nx][ny] = cost

    return distance[-1][-1]


i = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    graph = []

    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    min_distance = dijkstra(N, graph)
    answer1 = "Problem "
    answer2 = str(i) + ": "
    answer3 = str(min_distance)
    i += 1
    print(answer1 + answer2 + answer3)
