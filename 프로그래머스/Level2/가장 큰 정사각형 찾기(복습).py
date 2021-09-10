def solution(board):
    
    dp = [[0]*(len(board[0])) for _ in range(len(board))]
    dp[0] = board[0]
    for i in range(len(board)):
        dp[i][0] = board[i][0]
    
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    answer = 0
    for row in dp:
        answer = max( max(row) ,answer )
    
    return answer ** 2
