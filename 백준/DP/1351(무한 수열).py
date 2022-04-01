from collections import defaultdict
import sys
N, P, Q = map(int, sys.stdin.readline().split())
dp = defaultdict(int)
dp[0] = 1


def dfs(x):
    if dp[x] != 0:
        return dp[x]
    else:
        dp[x] = dfs(x//P) + dfs(x//Q)
        return dp[x]


dfs(N)
print(dp[N])

