# 정확성은 있지만 시간초과

def solution(number, k):
    count = 0
    number = list(number)   
    
    i = 0
    while i in range(len(number)-1):
        if count >= k :
            break
        if number[i] < number[i+1]:
            
            number = number[:i] + number[i+1:]
            count += 1
            if i == 0 : i = 0
            else : i -= 1
        else : i += 1
    
    answer = "".join(number)
    
    if count < k: answer = answer[:-k]
        
    return answer
