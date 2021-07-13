# 함정이 한번 있었던 문제. 예외처리를 잘 해야함.

def solution(n, lost, reserve):
    answer = 0
    solve = 0
    
    for l in lost:
        if l in reserve:
            solve += 1
            reserve.remove(l)
        elif l-1 in reserve:
            solve += 1
            reserve.remove(l-1)
        elif l+1 in reserve:
            if l+1 in lost:
                pass
            else :
                solve += 1
                reserve.remove(l+1)
        
    answer = n - len(lost) + solve
    return answer
