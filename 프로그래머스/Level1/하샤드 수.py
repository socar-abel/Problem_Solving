def solution(x):    
    num = [int(x) for x in list(str(x))]
    return True if x % sum(num) == 0 else False
