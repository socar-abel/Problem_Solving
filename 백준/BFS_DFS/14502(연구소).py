from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

points = []
virus = []
for a in range(N):
    for b in range(M):
        points.append((a, b))
        if graph[a][b] == 2: virus.append((a, b))

walls = list(combinations(points, 3))
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(wall):
    table = copy.deepcopy(graph)
    for i, j in wall:
        table[i][j] = 1

    q = deque()
    for v in virus:
        q.append((v[0], v[1]))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
                table[nx][ny] = 2
                q.append((nx, ny))

    count = 0
    # print('after bfs')
    # for x in table:
    #     print(x)

    for a in range(N):
        for b in range(M):
            if table[a][b] == 0: count += 1

    return count

answer = 0

for wall in walls:
    err = False
    for i, j in wall:
        if graph[i][j] == 2 or graph[i][j] == 1: err = True; break

    if err: continue
    # print('wall',wall)
    answer = max(answer, bfs(wall))

print(answer)

