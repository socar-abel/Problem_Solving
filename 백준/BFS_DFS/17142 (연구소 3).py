import sys
from itertools import combinations
from collections import deque
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = 987654321
answer = INF
N, M = map(int, sys.stdin.readline().split())
graph = []
inactivated_virus = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            inactivated_virus.append((i, j))

combis = list(combinations(inactivated_virus, M))

for combi in combis:
    visit = [[False] * N for _ in range(N)]
    q = deque()
    # 활성화
    for i, j in combi:
        q.append((i, j, 0))
        visit[i][j] = True
    temp_answer = 0
    # BFS 로 시간 검색
    while q:
        x, y, t = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, t + 1))
                    visit[nx][ny] = True
                    temp_answer = max(temp_answer, t + 1)
                elif graph[nx][ny] == 2:
                    q.append((nx, ny, t + 1))
                    visit[nx][ny] = True
    # 모든 빈 칸을 다 채운 건지 확인
    flag = True
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1 and not visit[i][j]:
                flag = False
                break

    if flag:
        answer = min(answer, temp_answer)

if answer == INF:
    print(-1)
else:
    print(answer)


