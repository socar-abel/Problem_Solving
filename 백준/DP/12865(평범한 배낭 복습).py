import sys
N, K = map(int, sys.stdin.readline().split())
things = []
dp = [[0] * N for _ in range(K+1)]

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    things.append((W, V))

for b in range(K+1):
    if b >= things[0][0]:
        dp[b][0] = things[0][1]

for b in range(K+1):
    for i in range(1, N):
        w, v = things[i]
        if b < w:
            dp[b][i] = dp[b][i-1]
        else:
            dp[b][i] = max(dp[b][i-1], dp[b-w][i-1] + v)

print(dp[-1][-1])
