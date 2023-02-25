import sys
N = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

for a in range(2, N+1):
    for b in range(10):
        dp[a][b] = sum(dp[a-1][:b+1])

print(sum(dp[-1]) % 10007)
