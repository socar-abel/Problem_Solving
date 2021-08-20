def solution(triangle):
    answer = 0
    maximum = [[0 for _ in range(x+1)] for x in range(len(triangle))]
    maximum[0][0] = triangle[0][0]
    
    for level in range(len(triangle)-1):
        for x in range(len(triangle[level])+1):
            now = triangle[level+1][x]
            if x == 0 : maximum[level+1][x] = maximum[level][x] + now
            elif x == len(triangle[level]) : maximum[level+1][x] = maximum[level][x-1] + now
            else :
                maximum[level+1][x] = max( maximum[level][x-1] + now , maximum[level][x] + now)
        
    
    return max(maximum[-1])
