import sys
T = int(sys.stdin.readline())


def program():
    n = int(sys.stdin.readline())
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(n+1):
        if i >= 1:
            dp[i] += dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
        if i >= 3:
            dp[i] += dp[i - 3]
    print(dp[-1])


for _ in range(T):
    program() 
