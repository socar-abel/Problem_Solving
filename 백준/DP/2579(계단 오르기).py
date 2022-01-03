import sys
N = int(sys.stdin.readline())
stairs = []

for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

if N == 1 or N == 2:
    print(sum(stairs))
else:
    dp = [[0]*2 for _ in range(N)]
    dp[0][0] = stairs[0]
    dp[0][1] = stairs[0]
    dp[1][0] = stairs[1]
    dp[1][1] = stairs[0] + stairs[1]

    for i in range(2, N):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]
        dp[i][1] = dp[i-1][0] + stairs[i]

    print(max(dp[-1]))

