def check(m,n,a,b,board):
    x = board[a][b]
    if x != 'X' and a+1 in range(m) and b+1 in range(n) and board[a+1][b] == x and board[a+1][b+1] == x and board[a][b+1] == x : return True
    else : return False

def solution(m, n, board):
    answer = 0
    game = True
    board = list(map(list,board))

    while True:
        # 지울게 있으면 지운다.
        removal = []
        num = 0
        
        for a in range(m):
            for b in range(n):
                if check(m,n,a,b,board):
                    removal.append((a,b)); removal.append((a+1,b))
                    removal.append((a,b+1)); removal.append((a+1,b+1))   
                else : num += 1
        
        if num == n*m : break
        removal_set = set(removal)        
        answer += len(removal_set)
        
        for a in range(m):
            for b in range(n):
                if (a,b) in removal: board[a][b] = 'X'
        
        removal = list(removal_set)
        #print('removal', removal)
        
        # 블록이 떨어져 공간을 채운다.        
        for b in range(n):
            tempList = [board[x][b] for x in range(m)]
            
            if not 'X' in tempList : continue
            else :
                charList = []
                XList = []
                
                for t in tempList:
                    if t == 'X' : XList.append(t)
                    else: charList.append(t)
                
                afterList = []
                for x in XList:
                    afterList.append(x)
                for c in charList:
                    afterList.append(c)
            
            for i in range(m):
                board[i][b] = afterList[i]
        
    
    return answer
