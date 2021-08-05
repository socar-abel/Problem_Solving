# 풀고보니 이건 2진법으로 나타냈을 때 1의 개수를 세는 문제였다.

def solution(n):
    answer = 0
    
    while True:
        if n == 1 : answer += 1; break
        
        if n % 2 == 1: n -= 1; answer += 1
        else : n //= 2

    return answer
