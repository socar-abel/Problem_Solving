def solution(a, b):
    answer = 0
    if a > b: a, b = b, a
    list = [x for x in range(a,b+1)]
    answer = sum(list)    
    return answer
