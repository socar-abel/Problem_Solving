import sys
N, K = map(int, sys.stdin.readline().split())
coins = []
dp = [0] * (K+1)
dp[0] = 1

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort()

for coin in coins:
    for i in range(1, K+1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[-1])
