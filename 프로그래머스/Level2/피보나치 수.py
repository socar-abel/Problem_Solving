def solution(n):
    dp = [-1]*(n+1)
    dp[0], dp[1], dp[2] = 0, 1, 1
    
    x = 3
    while True:
        if x < 3 : break
        if x == n+1 : break
        dp[x] = dp[x-1] + dp[x-2]
        x += 1
        
    return dp[n] % 1234567
