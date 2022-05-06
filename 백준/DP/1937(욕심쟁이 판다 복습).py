import sys
sys.setrecursionlimit(10**6)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(sys.stdin.readline())
graph = []
dp = [[-1] * N for _ in range(N)]
answer = 0

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def dfs(x, y):
    global answer
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[x][y] < graph[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    answer = max(answer, dp[x][y])
    return dp[x][y]


for i in range(N):
    for j in range(N):
        dfs(i, j)

#
# for x in dp:
#     print(x)

print(answer)
