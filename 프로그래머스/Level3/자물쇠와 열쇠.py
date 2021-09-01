def match(moveSet, lock, holes):
    M = len(moveSet); N = len(lock)
    answer = False
    for a in range(N-M+1):
        for b in range(N-M+1):
            count = 0;
            flag = True
            for x in range(M):
                for y in range(M):
                    if moveSet[x][y] == 1 and lock[x+a][y+b] == 0 : count += 1
                    elif moveSet[x][y] == 1 and lock[x+a][y+b] == 1 : flag = False; break
                    
            if count >= holes and flag == True: return True
            
    return answer
    

def rotate(key): # 90도
    M = len(key)
    rotated = [[-1] * M for _ in range(M)]
    for a in range(M):
        for b in range(M):
            rotated[a][b] = key[M-1-b][a]
    return rotated

def getMoveSet(key,M):  # 움직여서 얻을 수 있는 모든 key 반환
    moved = []
    # moved 는 M + M-1 개
    total = [[0]*(3*M-2) for _ in range(3*M-2+1)]
    
    for x in range(M-1, 2*M-1):
        for y in range(M-1, 2*M-1):
            total[x][y] = key[x-(M-1)][y-(M-1)]
    
    for a in range(2*M-2+1):
        for b in range(2*M-2+1):
            temp = [[-1]*M for _ in range(M)]
            for x in range(M):
                for y in range(M):
                    temp[x][y] = total[x+a][y+b]
            moved.append(temp) 
    
    return moved        
            

def solution(key, lock):
    answer = False
    M = len(key); N = len(lock)
    
    holes = 0
    for a in range(N):
        for b in range(N):
            if lock[a][b] == 0 : holes += 1
    
    rotateSet = [key, rotate(key), rotate(rotate(key)), rotate(rotate(rotate(key)))]
    
    for k in rotateSet:
        moveSets = getMoveSet(k,M)

        for moveSet in moveSets:
            if match(moveSet, lock, holes) : return True
        
                    
    
    return answer
