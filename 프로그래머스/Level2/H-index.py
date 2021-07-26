def solution(citations):
    answer = 0
    citations.sort()
    
    for h in range(len(citations)+1):
        if citations[-h] >= h: answer = h
    
    return answer
