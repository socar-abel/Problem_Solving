import sys
sys.setrecursionlimit(10**6)
N, L = map(int, sys.stdin.readline().split())
dp = [[-1] * (L+1) for _ in range(N+1)]
MOD = 100030001


# n개의 볼로 높이 k 이하의 트리 만들기
def solve(n, k):
    if n == 0:
        return 1
    if k == 0:
        return 0
    if dp[n][k] != -1:
        return dp[n][k]

    dp[n][k] = 0
    for i in range(n):
        dp[n][k] += solve(i, k-1) * solve(n-i-1, k-1)
        dp[n][k] %= MOD
    return dp[n][k]


print((solve(N, L) - solve(N, L-1) + MOD) % MOD)


