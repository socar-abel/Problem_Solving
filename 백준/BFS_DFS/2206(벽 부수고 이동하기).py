from collections import deque
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, sys.stdin.readline().split())
graph = []
visit = [[[False, False] for _ in range(M)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

q = deque()
q.append((0, 0, 1, 0))
# (x, y) 를 벽을 이미 한 번 부순 상태로 방문했으면 visit[x][y][1] = True
# (x, y) 를 벽을 아직 부순적 없는 상태로 방문했으면 visit[x][y][0] = True
visit[0][0][0] = True
can_reach = False
answer = 0

while q:
    x, y, dist, wall = q.popleft()

    if x == N-1 and y == M-1:
        can_reach = True
        answer = dist
        break

    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        if not(0 <= nx < N and 0 <= ny < M):
            continue

        if wall == 0 and not visit[nx][ny][0]:
            if graph[nx][ny] == 0:
                q.append((nx, ny, dist+1, wall))
            elif graph[nx][ny] == 1:
                q.append((nx, ny, dist+1, wall + 1))
            visit[nx][ny][0] = True

        elif wall == 1 and not visit[nx][ny][1]:
            if graph[nx][ny] == 0:
                q.append((nx, ny, dist+1, wall))
                visit[nx][ny][1] = True
            elif graph[nx][ny] == 1:
                continue


if not can_reach:
    print(-1)
else:
    print(answer)
