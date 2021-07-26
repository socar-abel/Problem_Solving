def solution(brown, yellow):
    answer = []
    yellowXY = []
    
    if yellow == 1:
        return [3,3]
        
    else:
        for x in range(1,yellow//2+1):
            if yellow % x == 0:
                y = yellow // x
                yellowXY.append((y,x))
    
    for x,y in yellowXY:
        if (x*2) + (y*2) + 4 == brown : 
            answer = [x+2,y+2]
            break
    
    
    return answer
