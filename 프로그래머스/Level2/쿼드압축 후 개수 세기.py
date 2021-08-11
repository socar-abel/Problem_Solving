# 피지컬 향상 중 . . .
zero, one = 0, 0

def compress(S):
    print('현재 S')
    print(S)
    global zero; global one
    # 재귀탈출
    if len(S) == 1 : 
        if S[0][0] == 0: zero += 1; print('1칸 짜리, zero ++')
        elif S[0][0] == 1: one += 1; print('1칸 짜리, one ++')
        return
    print()
    # step2
    print('step2 검사')
    tempZero, tempOne = 0,0
    l = len(S)
    for a in range(l):
        for b in range(l):
            if S[a][b] == 0 : tempZero += 1
            elif S[a][b] == 1 : tempOne += 1
    if tempZero == l*l : zero += 1; print('0압축'); print(); return
    elif tempOne == l*l : one += 1; print('1압축'); print(); return
    
    print('step3 진행')
    print()
    # step3
    S1, S2 = [[] for _ in range(l//2)], [[] for _ in range(l//2)]
    S3, S4 = [[] for _ in range(l//2)], [[] for _ in range(l//2)]
    for a in range(l):
        for b in range(l):
            #print('a,b',a,b)
            if a < l//2 and b < l//2 : S1[a].append(S[a][b]);
            elif a < l//2 and b >= l//2 : S2[a].append(S[a][b]); 
            elif a >= l//2 and b < l//2 : S3[a%(l//2)].append(S[a][b]);
            else : S4[a%(l//2)].append(S[a][b]); 
    compress(S1); compress(S2); compress(S3); compress(S4);
    

def solution(arr):
    answer = [0,0]
    global zero; global one
    
    compress(arr)
    
    answer[0] = zero; answer[1] = one
    return answer




print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
