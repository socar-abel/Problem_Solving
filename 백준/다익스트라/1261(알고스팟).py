import sys
import heapq
M, N = map(int, sys.stdin.readline().split())
graph = []
INF = 987654321
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

for _ in range(N):
    input = sys.stdin.readline().strip()
    a = []
    for x in input:
        a.append(int(x))
    graph.append(a)


def adjacent(x, y):
    nodes = []
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            nodes.append((nx, ny))
    return nodes


# 다익스트라
distance = [[INF]*M for _ in range(N)]
distance[0][0] = 0

q = []

for x, y in adjacent(0, 0):
    # 최단거리 테이블 세팅
    distance[x][y] = graph[x][y]
    # 힙에 푸시. 거리, 노드 좌표
    heapq.heappush(q, (graph[x][y], x, y))

while q:
    d, x, y = heapq.heappop(q)
    if distance[x][y] < d:
        continue

    for nx, ny in adjacent(x, y):
        cost = d + graph[nx][ny]
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[-1][-1])

