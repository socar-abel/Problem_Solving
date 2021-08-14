# 다이나믹 프로그래밍 어느정도 극복한듯하다
def solution(land):
    answer = 0
    dp = [[0]*4 for _ in range(len(land))]
    dp[0] = land[0]
    
    for i in range(1,len(land)):
        for x in range(4):
            dp[i][x] = max(dp[i-1][:x]+dp[i-1][x+1:]) + land[i][x]

    return max(dp[-1])
