# 입력 조건이 백만이어서 이진탐색 해야하나 했는데 그냥 순차탐색으로 풀림 ..;

def solution(arr):
    answer = []
    
    now = arr[0]
    answer.append(now)
    
    i = 1
    while i < len(arr):
        if arr[i] == now :
            pass
        else:
            now = arr[i]
            answer.append(now)
        i += 1
        
        
    return answer
