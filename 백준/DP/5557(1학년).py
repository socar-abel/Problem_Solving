import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0] * 21 for _ in range(N)]
dp[0][arr[0]] = 1

for i in range(1, N):
    for j in range(21):
        if j - arr[i] >= 0:
            dp[i][j] += dp[i-1][j-arr[i]]
        if j + arr[i] <= 20:
            dp[i][j] += dp[i-1][j+arr[i]]

print(dp[N-2][arr[-1]])
