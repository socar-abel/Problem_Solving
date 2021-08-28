def check(x):
    count = 0
    for i in range(1,x+1):
        if x % i == 0: count += 1
    return -1 if count % 2 == 1 else 1

def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        answer += x * check(x)
    
    return answer
