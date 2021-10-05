import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

def bfs(a, b, graph, visit):
    unit = []  # 연합에 가입한 나라 좌표
    people = 0  # 나라 인구수의 합

    q = deque()
    q.append((a, b))
    unit.append((a, b))
    people += graph[a][b]
    visit[a][b] = True

    while q:
        x, y = q.popleft()

        for d in direction:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    q.append((nx, ny))
                    unit.append((nx, ny))
                    people += graph[nx][ny]
                    visit[nx][ny] = True

    newPeople = people // len(unit)

    for a, b in unit:
        graph[a][b] = newPeople

    return True if len(unit) >= 2 else False


day = 0
while True:
    visit = [[False] * N for _ in range(N)]
    stop = True  # stop이 True면 while문 종료

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                check = bfs(i, j, graph, visit)
                if check:
                    stop = False

    if stop:
        break
    else:
        day += 1

print(day)
