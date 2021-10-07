import sys
N = int(sys.stdin.readline())

if N == 1:
    print(0)
    exit(0)
elif N == 2 or N == 3:
    print(1)
    exit(0)

dp = [0]*(N+1)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i-1], dp[i//3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])
