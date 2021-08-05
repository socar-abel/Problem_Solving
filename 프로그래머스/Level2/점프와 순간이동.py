def solution(n):
    answer = 0
    
    while True:
        if n == 1 : answer += 1; break
        
        if n % 2 == 1: n -= 1; answer += 1
        else : n //= 2

    return answer
