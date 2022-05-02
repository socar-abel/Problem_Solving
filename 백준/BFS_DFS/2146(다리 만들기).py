from collections import deque
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(sys.stdin.readline())
graph = []
island = [[-1] * N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


temp_island = 0
visit = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visit[i][j] and graph[i][j] == 1:
            # BFS 로 섬 담기
            q = deque()
            q.append((i, j))
            visit[i][j] = True

            while q:
                x, y = q.popleft()
                island[x][y] = temp_island

                for d in direction:
                    nx = x + d[0]
                    ny = y + d[1]

                    if 0 <= nx < N and 0 <= ny < N:
                        if not visit[nx][ny] and graph[nx][ny] == 1:
                            q.append((nx, ny))
                            visit[nx][ny] = True

            temp_island += 1


answer = 987654321
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            v = [[False] * N for _ in range(N)]
            q = deque()
            q.append((i, j, 0))
            v[i][j] = True

            while q:
                x, y, dist = q.popleft()

                if graph[x][y] == 1 and (island[i][j] != island[x][y]):
                    answer = min(answer, dist - 1)
                    break

                for d in direction:
                    nx = x + d[0]
                    ny = y + d[1]

                    if 0 <= nx < N and 0 <= ny < N and not v[nx][ny]:
                        if graph[nx][ny] == 0:
                            q.append((nx, ny, dist + 1))
                        elif graph[nx][ny] == 1 and (island[i][j] != island[nx][ny]):
                            q.append((nx, ny, dist + 1))
                        v[nx][ny] = True

print(answer)
