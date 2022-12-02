import sys
s = sys.stdin.readline().strip()
N = len(s)
is_pd = [[False]*N for _ in range(N)]
dp = [1]*N

for i in range(N):
    for j in range(N):
        if s[i:j+1] == s[i:j+1][::-1]:
            is_pd[i][j] = True

for i in range(1, N):
    dp[i] = dp[i-1] + 1
    if is_pd[0][i]:
        dp[i] = 1
        continue
    for k in range(i):
        if is_pd[k+1][i]:
            dp[i] = min(dp[i], dp[k] + 1)

print(dp[-1])
