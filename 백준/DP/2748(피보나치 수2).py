import sys
N = int(sys.stdin.readline())

if N == 1:
    print(1)
else:
    dp = [0] * (N+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[N])
