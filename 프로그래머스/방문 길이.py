def solution(dirs):
    answer = 0
    already = []
    character = (0,0)
    
    for d in dirs:
        x, y = character[0], character[1]
        nx, ny = x, y
        if d == 'U' : ny += 1
        elif d == 'D' : ny -= 1
        elif d == 'R' : nx += 1
        elif d == 'L' : nx -= 1
        
        if (not( -5 <= nx <= 5)) or (not(-5 <= ny <= 5)) : continue
        path = (x,y,nx,ny)
        if not path in already : 
            already.append((x,y,nx,ny))
            already.append((nx,ny,x,y))
            answer += 1    
        character = (nx, ny)
    
    return answer
