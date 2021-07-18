def solution(num):
    count = 0
    while num != 1:
        if count == 500:
            count = -1
            break
        
        count += 1
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num*3) + 1
        
    
    return count
