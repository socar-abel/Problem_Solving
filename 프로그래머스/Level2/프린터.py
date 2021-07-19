from collections import deque

def solution(priorities, location):
    pdeque = deque([(True,priorities[i]) if i == location else (False,priorities[i]) for i in range(len(priorities))])
    
    count = 0
    while pdeque:
        now = pdeque[0]
        
        if max(pdeque, key = lambda x : x[1])[1] > now[1]:
            pdeque.popleft()
            pdeque.append(now)
        else:
            pdeque.popleft()
            count += 1
            if now[0] == True:
                break
            
    
    return count
