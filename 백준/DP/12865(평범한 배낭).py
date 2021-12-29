import sys
N, K = map(int, sys.stdin.readline().split())
gems = []

for _ in range(N):
    # W, V
    gems.append(tuple(map(int, sys.stdin.readline().split())))

# dp[i][j] = i 번째 까지 탐색 했을 때, 무게 j 인 가방의 최대 가치
dp = [[0]*(K+1) for _ in range(N)]
for i in range(N):
    dp[i][0] = 0
for j in range(K+1):
    if gems[0][0] <= j:
        dp[0][j] = gems[0][1]

for i in range(1, N):
    for j in range(1, K+1):
        if gems[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-gems[i][0]]+gems[i][1])

print(dp[-1][-1])
