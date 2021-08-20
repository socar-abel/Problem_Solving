def solution(N, number):
    answer = -1
    
    canMakeBy = [[] for _ in range(9)]
    
    canMakeBy[0] = [0]
    canMakeBy[1] = [N]
    canMakeBy[2] = [10*N+N,N+N,N-N,N*N,N//N]
    
    for i in range(3,9):
        combo = N
        for x in range(2,i+1):
            combo += N * (10**(x-1))
        canMakeBy[i].append(combo)
        '''
        for x in canMakeBy[i-1]:
            canMakeBy[i].append(x+N)
            canMakeBy[i].append(x-N)
            canMakeBy[i].append(x*N)
            canMakeBy[i].append(x//N)
        '''
        # { 3 : (1+2) } { 4 : (1+3), (2+2) } { 5 : (1+4), (2+3) } 
        for j in range(1, (i//2)+1):
            setA = canMakeBy[j]; setB = canMakeBy[i-j]
            for a in setA:
                for b in setB:
                    if a != 0 and b != 0 :
                        canMakeBy[i].append(a+b)
                        canMakeBy[i].append(abs(a-b))
                        canMakeBy[i].append(a//b)
                        canMakeBy[i].append(b//a)
                    canMakeBy[i].append(a*b)
    for i in range(9):
        if number in canMakeBy[i] : answer = i; break;
    
    return answer
