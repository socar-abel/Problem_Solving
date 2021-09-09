# 예전보다 수월하게 품

def solution(n):
    answer = []
    tri = [[-1]*(x+1) for x in range(n)]
    dirs = [(1,0),(0,1),(-1,-1)] # Up, Right, Down
    turn = n; count = 0
    x, y = 0, 0; d = 0; a = 1
    
    while a <= n*(n+1)//2:
        tri[x][y] = a; count += 1
        if count == turn : turn -= 1; count = 0; d = (d+1) % 3
            
        x = x + dirs[d][0]
        y = y + dirs[d][1]
        
        a += 1

    return sum(tri, [])
