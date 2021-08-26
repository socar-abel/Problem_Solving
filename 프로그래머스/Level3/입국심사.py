def solution(n, times):
    answer = 0
    left = 1; right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2; result = 0
        
        for time in times :
            result += mid // time
            
        if result >= n : right = mid - 1
        else : left = mid + 1
    
    return left
