# 투 포인터 사용 - 효율성 1개 통과함 ㅋㅋ
from collections import deque

def solution(gems):
    answer = [0,len(gems)]
    
    kindOfgems = len(set(gems)) # O(n)
    start = 0
    end = 0
    
    tempSum = deque()
    for start in range(len(gems)):
        while len(set(tempSum)) < kindOfgems and end < len(gems):
            tempSum.append(gems[end])
            end += 1
                    
        if len(set(tempSum)) == kindOfgems:
            if end - (start+1) < (answer[1]-answer[0]): 
                answer=[start+1,end]
            elif end - (start+1) == (answer[1]-answer[0]): 
                if start+1 < answer[0]:
                    answer = [start+1,end]
                else:
                    pass
            
        tempSum.popleft()
            
    
    
    return answer
