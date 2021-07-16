# 반드시 복습해봐야 할 문제. while문 활용 + 문제 자세히 읽기 + 다 조건 다루기 등 많은 것을 배움. deque는 사용하지 않았음. 

from collections import deque

def solution(dartResult):
    answer = 0
    buffer = -1
    score = []
    
    i = 0
    while i < len(dartResult):
        now = dartResult[i]
        
        if now.isdigit():
            if now == '0' and i > 0:
                if dartResult[i-1] == '1':
                    buffer = 10
                    score[-1] = buffer
                else:
                    buffer = 0
                    score.append(buffer)
            else:
                buffer = int(now)
                score.append(buffer)
        else:
            if now == 'S':
                score[-1] = score[-1]
            elif now == 'D':
                score[-1] = score[-1] ** 2
            elif now == 'T':
                score[-1] = score[-1] ** 3
            elif now == '*':
                if len(score) >= 2:
                    score[-1] *= 2
                    score[-2] *= 2
                else:
                    score[-1] *= 2
            elif now == '#':
                score[-1] *= (-1)
        i += 1
                
    answer = sum(score)
    
    return answer
