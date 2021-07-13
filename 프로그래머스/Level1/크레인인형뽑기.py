def solution(board, moves):
    answer = 0
    stack = [-1]
    size = len(board[0])
    
    for move in moves:
        for i in range(size):
            temp = board[i][move-1]
            if not temp == 0:
                stack.append(temp)
                board[i][move-1] = 0
                
                if len(stack) >= 3 and (stack[-1]==stack[-2]):
                    stack.pop()
                    stack.pop()
                    answer += 1
                break
        
            
    return answer*2
