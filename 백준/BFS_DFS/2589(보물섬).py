from collections import deque
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, sys.stdin.readline().split())
graph = []
answer = 0

for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'W':
            continue
        #print('BFS', i, j)
        visit = [[False] * M for _ in range(N)]
        q = deque()
        q.append((i, j, 0))
        visit[i][j] = True
        temp_max = 0

        while q:
            x, y, dist = q.popleft()
            #print('x y dist', x, y, dist)
            temp_max = max(temp_max, dist)

            for d in direction:
                nx = x + d[0]
                ny = y + d[1]

                if 0 <= nx < N and 0 <= ny < M:
                    if not visit[nx][ny] and graph[nx][ny] == 'L':
                        q.append((nx, ny, dist + 1))
                        visit[nx][ny] = True

        #print(temp_max)
        answer = max(answer, temp_max)


print(answer)
