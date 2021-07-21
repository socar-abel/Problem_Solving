def solution(n):
    answer = ''
    
    numbers = ['1','2','4']
    
    while n > 0 :
        
        n -= 1
        
        answer = numbers[n%3] + answer
        
        n //= 3
        
    
    return answer
