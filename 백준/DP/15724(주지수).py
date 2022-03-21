import sys
N, M = map(int, sys.stdin.readline().split())
graph = []
dp = [[0] * M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

K = int(sys.stdin.readline())
query = []

for _ in range(K):
    l = list(map(int, sys.stdin.readline().split()))
    query.append((l[0]-1, l[1]-1, l[2]-1, l[3]-1))


# dp 초기 세팅
dp[0][0] = graph[0][0]

for j in range(1, M):
    dp[0][j] = dp[0][j-1] + graph[0][j]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + graph[i][0]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i][j]

for a, b, c, d in query:
    if a == 0 and b == 0:
        print(dp[c][d])
    else:
        if a == 0:
            print(dp[c][d] - dp[c][b-1])
        elif b == 0:
            print(dp[c][d] - dp[a-1][d])
        else:
            print(dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1])


