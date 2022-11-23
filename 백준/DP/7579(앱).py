import sys
INF = 987654321
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))
apps = [(a, c) for a, c in zip(A, C)]
apps.sort(key=lambda x: x[1])
dp = [[0] * (N*101) for _ in range(N)]

for i in range(N*101):
    if i >= apps[0][1]:
        dp[0][i] = apps[0][0]

for i in range(1, N):
    m, c = apps[i][0], apps[i][1]
    for j in range(N*101):
        if j >= c:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + m)
        else:
            dp[i][j] = dp[i-1][j]

answer = INF
for i in range(N):
    for j in range(N*101):
        if dp[i][j] >= M:
            answer = min(answer, j)
            break

print(answer)

