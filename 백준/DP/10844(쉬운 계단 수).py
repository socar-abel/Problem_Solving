import sys
from collections import deque
N = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for n in range(2, N+1):
    for i in range(10):
        if i == 0:
            dp[n][i] = dp[n-1][1]
        elif i == 9:
            dp[n][i] = dp[n-1][8]
        else:
            dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1]

print(sum(dp[-1]) % (10**9))
