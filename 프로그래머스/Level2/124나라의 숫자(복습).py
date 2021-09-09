def solution(n):
    answer = ''
    number = ['1','2','4']
    
    while n > 0:
        n -= 1
        answer = number[n%3] + answer
        n //= 3
    
    return answer
