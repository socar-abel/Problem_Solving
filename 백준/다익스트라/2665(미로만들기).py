import sys
import heapq
INF = sys.maxsize
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
distance = [[INF] * N for _ in range(N)]
distance[0][0] = 0
q = []
heapq.heappush(q, (0, 0, 0))

while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
        continue
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < N and 0 <= ny < N:
            cost = dist if graph[nx][ny] == 1 else dist + 1
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

print(distance[-1][-1])
