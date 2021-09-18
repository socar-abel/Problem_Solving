# 앞에서 뒤로
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * M for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))
# print('<dp table>')
# for x in dp:
#     print(x)
#
#
#
# print(dfs(0, 0))
