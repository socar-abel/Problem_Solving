import sys
N = int(sys.stdin.readline())
house = []
dp = [[0]*3 for _ in range(N)]

for _ in range(N):
    house.append(tuple(map(int, sys.stdin.readline().split())))

dp[0] = house[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]

print(min(dp[-1]))
