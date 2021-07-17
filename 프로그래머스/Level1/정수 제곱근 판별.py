def solution(n):
    answer = 0
    if ((n**0.5)*10)%10 == 0 : answer = ((n**0.5)+1)**2
    else : answer = -1
    return answer
