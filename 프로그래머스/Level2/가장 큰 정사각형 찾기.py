def solution(board):
    maxSide = 0
    row = len(board)
    col = len(board[0])
    
    dp = [ [0] * col for _ in range(row) ]
    
    for a in range(row):
        dp[a][0] = board[a][0]
    dp[0] = board[0]
    
    for a in range(1, row):
        for b in range(1, col):
            if board[a][b] == 1:
                dp[a][b] = min(dp[a-1][b-1], dp[a-1][b], dp[a][b-1]) + 1
            
    for a in dp:
        if max(a) > maxSide : maxSide = max(a)
    
    #print(dp)
    return maxSide ** 2
