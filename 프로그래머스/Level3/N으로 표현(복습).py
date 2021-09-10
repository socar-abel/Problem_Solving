def solution(N, number):
    answer = -1
    candidates = [[] for _ in range(9)]
    candidates[1] = [N]
    
    for i in range(2,9):
        candidates[i].append(int(str(N)*i))
        
        for x in range(1, i//2+1): 
            for a in candidates[x]:
                for b in candidates[i-x]:
                    candidates[i].append(a+b)
                    candidates[i].append(a-b)
                    candidates[i].append(b-a)
                    candidates[i].append(a*b)
                    if b != 0 : candidates[i].append(a//b)
                    if a != 0 : candidates[i].append(b//a)


    for i in range(len(candidates)):
        if number in candidates[i]: return i

    return answer
