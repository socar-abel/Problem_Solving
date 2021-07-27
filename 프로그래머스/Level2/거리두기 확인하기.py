def solution(places):
    answer = []
    distance1 = [(-1,0), (1,0), (0,-1), (0,1)] #상하좌우
    distance2_1 = [(-2,0), (2,0), (0,-2), (0,2)] #상하좌우
    distance2_2 = [(-1,-1), (1,1), (1,-1), (1,1)] 
    
    for place in places:
        result = 1
        for x in range(5):
            for y in range(5):
                
                if place[x][y] == 'P':
                    for d1 in distance1:
                        nx = x + d1[0]
                        ny = y + d1[1]
                        if nx in range(5) and ny in range(5) and place[nx][ny] == 'P':
                            result = 0
                            break
                    for d2 in distance2_1:
                        nx = x + d2[0]
                        ny = y + d2[1]
                        mx = x + d2[0]//2
                        my = y + d2[1]//2
                        if nx in range(5) and ny in range(5) and place[nx][ny] == 'P':
                            if place[mx][my] == 'O':
                                result = 0
                                break
                    for d2 in distance2_2:
                        nx = x + d2[0]
                        ny = y + d2[1]
                        
                        if nx in range(5) and ny in range(5) and place[nx][ny] == 'P':
                            if place[nx][y] == 'O' or place[x][ny] == 'O':
                                result = 0
                                break
        answer.append(result)
        
    
    return answer
