# 투 포인터 알고리즘엔 문제가 없다. dict를 사용해야 할 뿐
from collections import deque

def solution(gems):
    candidates = []
    gemType = len(set(gems))
    shopping = dict()
    start, end = 0, 0
    
    for start in range(len(gems)):
        while end < len(gems) and len(shopping) < gemType:
            if not gems[end] in shopping:
                shopping[gems[end]] = 1
            else: shopping[gems[end]] += 1
            end += 1
        
        if len(shopping) == gemType:
            candidates.append([start,end])
            shopping[gems[start]] -= 1
            if shopping[gems[start]] == 0: del shopping[gems[start]]

    
    candy = min(candidates, key = lambda x : x[1]-x[0])
    return [candy[0]+1,candy[1]]
