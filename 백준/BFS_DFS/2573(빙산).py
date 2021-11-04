import sys
from collections import deque
direction = [(-1,0), (1,0), (0,-1), (0,1)]

N, M = map(int, sys.stdin.readline().split())
graph = []
visit = [[False]*M for _ in range(N)]
melt = [[0]*M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

year = 0
while True:
    # print('current situation')
    # for x in graph:
    #     print(x)

    # 초기화
    for i in range(N):
        for j in range(M):
            visit[i][j] = False
            melt[i][j] = 0

    # 빙산 개수 탐색
    ice = 0
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and graph[i][j] > 0:
                #print('bfs start',i,j)
                q = deque()
                q.append((i,j))
                visit[i][j] = True

                while q:
                    x, y = q.popleft()
                    ocean = 0
                    for d in direction:
                        nx = x + d[0]
                        ny = y + d[1]

                        if 0<=nx<N and 0<=ny<M:
                            if graph[nx][ny] <= 0:
                                ocean += 1
                            if not visit[nx][ny] and graph[nx][ny] > 0:
                                q.append((nx,ny))
                                #print('append',nx,ny)
                                visit[nx][ny] = True

                    melt[x][y] = ocean
                ice += 1

    # 종료 조건
    if ice >= 2:
        print(year)
        break
    elif ice == 0:
        print(0)
        break


    #print('year ice',year,ice)

    # 빙산 녹이기
    for i in range(N):
        for j in range(M):
            graph[i][j] -= melt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    year += 1
