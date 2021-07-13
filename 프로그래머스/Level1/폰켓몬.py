from collections import Counter

def solution(nums):
    answer = 0
    N = len(nums)
    
    counter = Counter(nums)
    
    if len(counter) <= N//2:
        answer = len(counter)
    else :
        answer = N//2
    
    return answer
