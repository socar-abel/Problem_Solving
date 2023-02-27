def solution(x, y, n):
    INF = 987654321
    dp = [INF] * (y + 1)
    dp[x] = 0
    for i in range(x + 1, y + 1):
        if i - n > 0:
            dp[i] = min(dp[i], dp[i - n] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    
    return dp[y] if dp[y] != INF else -1
