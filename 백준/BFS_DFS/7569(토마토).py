from collections import deque
import sys
direction = [(0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0)]
N, M, H = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(H)]
adult_tomato = []

for h in range(H):
    for m in range(M):
        input_list = list(map(int, sys.stdin.readline().split()))
        graph[h].append(input_list)
        for n in range(N):
            if input_list[n] == 1:
                adult_tomato.append((m, n, h))

answer = 0
visit = [[[False]*N for _ in range(M)] for _ in range(H)]
q = deque()

for t in adult_tomato:
    # x, y, z 좌표, 날짜
    q.append((t[2], t[0], t[1], 0))
    visit[t[2]][t[0]][t[1]] = True

while q:
    z, x, y, day = q.popleft()
    answer = max(answer, day)

    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        nz = z + d[2]

        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and not visit[nz][nx][ny]:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1
                visit[nz][nx][ny] = True
                q.append((nz, nx, ny, day + 1))


all_adult = True
for i in range(M):
    for j in range(N):
        for k in range(H):
            if graph[k][i][j] == 0:
                all_adult = False

if all_adult:
    print(answer)
else:
    print(-1)
