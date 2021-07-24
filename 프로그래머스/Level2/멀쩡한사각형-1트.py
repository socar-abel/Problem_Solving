# 정확성은 맞았지만, 효율성이 틀린 코드

import math
def solution(w,h):
    answer = 0
    
    table = [[0] * h for _ in range(w)]
    
    m = h / w
    
    first = (0,0)
    
    for _ in range(w):
        x = first[0]
        second = (x+1, m*(x+1))
        
        y = math.floor(first[1])
        while True:
            if math.floor(first[1]) <= y < second[1]:
                # print(x,y)
                table[x][y] = 1
                y += 1
            else : break
                
        first = second
    
    for i in range(w):
        answer += table[i].count(0)
    
    return answer
