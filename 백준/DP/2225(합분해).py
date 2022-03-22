import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(K+1):
    dp[0][i] = 0
    dp[1][i] = i

for i in range(N+1):
    dp[i][0] = 0
    dp[i][1] = 1

for n in range(2, N+1):
    for k in range(2, K+1):
        dp[n][k] = dp[n-1][k] + dp[n][k-1]

print(dp[N][K] % 1000000000)

