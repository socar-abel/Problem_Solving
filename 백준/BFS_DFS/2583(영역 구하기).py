import sys

sys.setrecursionlimit(10 ** 6)
M, N, K = map(int, sys.stdin.readline().split())

graph = [[0] * N for _ in range(M)]

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())

    for a in range(x1, x2):
        for b in range(y1, y2):
            graph[a][b] = 1

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[False] * N for _ in range(M)]

def dfs(x, y, visit):
    visit[x][y] = True
    global S
    S += 1

    for d in direction:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 0 and not visit[nx][ny]:
                dfs(nx, ny, visit)


answer = 0
scopes = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visit[i][j]:
            S = 0
            dfs(i, j, visit)
            answer += 1
            scopes.append(S)


print(answer)
print(" ".join(list(map(str, sorted(scopes)))))
