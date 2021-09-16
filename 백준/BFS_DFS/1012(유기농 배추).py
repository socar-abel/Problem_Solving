import sys
sys.setrecursionlimit(3000)

T = int(input())
while T > 0:
    M, N, K = map(int, input().split())

    graph = [[0]*N for _ in range(M)]
    visited = [[False]*N for _ in range(M)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    # for x in graph:
    #     print(x)

    def dfs(x, y):
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited[x][y] = True
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


    count = 0

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1 and not visited[a][b]:
                dfs(a, b); count += 1

    print(count)

    T -= 1
