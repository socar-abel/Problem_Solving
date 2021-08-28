# 이진탐색으로 구현 안해도 효율성 테스트 통과는 하는 듯 하다.
# Level 1은 아니고 Level 2 정도? 되는 듯
import bisect
def solution(N, stages):
    stages.sort()
    failure = [-1] * (N+1)
    
    for x in range(1, N+1):
        left = bisect.bisect_left(stages, x)
        right = bisect.bisect_right(stages, x)
        
        notClear = right - left
        reach = len(stages) - left
        if reach == 0: failure[x] = 0
        else : failure[x] = notClear / reach 
    
    enums = []
    for enum in enumerate(failure):
        enums.append(enum)
    
    enums.sort(key = lambda x : x[1], reverse = True)
    return list(map(lambda x : x[0], enums[:-1]))
