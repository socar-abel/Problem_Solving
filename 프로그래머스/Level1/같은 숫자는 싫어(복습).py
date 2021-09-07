def solution(arr):
    answer = [arr[0]]
    
    for x in arr[1:]:
        if x == answer[-1]: continue
        else: answer.append(x)
    
    return answer
