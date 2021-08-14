def solution(n):
    if n == 1 : return 1
    answer = 1
    numbers = [x for x in range(1,n+1)]
    
    start, end = 0, 1
    while True:
        if end >= len(numbers) or start == end : break
        if sum(numbers[start:end+1]) < n : end += 1
        elif sum(numbers[start:end+1]) == n : end += 1; start += 1; answer += 1
        else : start += 1
    return answer
