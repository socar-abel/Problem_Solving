from collections import deque

def solution(maps):
    answer = -1
    q = deque()
    n = len(maps)
    m = len(maps[0])
    direction = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우
    
    position = (0,0)
    q.append(position)
    
    while q:    
        now = q.popleft()
        
        for d in direction:
            nx = now[0] + d[0]
            ny = now[1] + d[1]
            
            if nx in range(n) and ny in range(m) and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] += maps[now[0]][now[1]]
                if nx == n-1 and ny == m-1 : 
                    answer = maps[nx][ny]
                    break
    
    
    #print(maps)            
    
    return answer
