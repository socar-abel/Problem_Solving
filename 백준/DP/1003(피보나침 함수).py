import sys
T = int(sys.stdin.readline())


def program(n):
    if n == 0:
        print(1, 0)
        return
    elif n == 1:
        print(0, 1)
        return

    dp = [[0]*2 for _ in range(n+1)]
    dp[0][0], dp[0][1] = 1, 0
    dp[1][0], dp[1][1] = 0, 1

    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    print(dp[n][0], dp[n][1])


for _ in range(T):
    N = int(sys.stdin.readline())
    program(N)
