def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        low, now = -1, prices[i]
        
        for j in range(i+1,len(prices)):
            if now > prices[j]:
                low = j; break;
        
        if low == -1 : answer.append(len(prices)-i-1)
        else : answer.append(low-i)
    
    
    return answer
