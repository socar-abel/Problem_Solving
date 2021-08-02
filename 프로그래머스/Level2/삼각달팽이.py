def solution(n):
    tri = [[0 for _ in range(i)] for i in range(n+1)]
    
    side = ['left','bottom','right']
    x, y, s = 0, 0, 0
    num, step = 1, n
    
    while True:
        if num > (n*(n+1))//2 : break    
        i = 0
        while i < step:
            if side[s] == 'left':
                x += 1
                tri[x][y] = num
                num += 1; i += 1
            elif side[s] == 'bottom':
                y += 1
                tri[x][y] = num
                num += 1; i += 1
            elif side[s] == 'right':
                x -= 1; y -= 1
                tri[x][y] = num
                num += 1; i += 1
        s = (s+1)%3
        step -= 1
    
    return sum(tri,[])
