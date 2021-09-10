# 투포인터로 풀었지만 시간복잡도 실패
from collections import deque
def solution(gems):
    candidates = []
    gemType = len(set(gems))
    start, end = 0, 0
    
    for start in range(len(gems)):
        while end < len(gems) and len(set(gems[start:end+1])) < gemType:
            end += 1
        
        if len(set(gems[start:end+1])) == gemType:
            candidates.append([start,end])
    
    candy = min(candidates, key = lambda x : x[1]-x[0])
    return [candy[0]+1,candy[1]+1]
