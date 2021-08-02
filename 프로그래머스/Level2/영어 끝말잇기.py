def solution(n, words):
    answer = [0,0]
    used = []
    fail = 0
    before = words[0][0]
    #print(before)
    
    for i in range(len(words)):
        if not before[-1] == words[i][0]:
            fail = i
            answer[1] = (fail // n) + 1
            answer[0] = (fail % n) + 1
            break
        
        if words[i] in used :
            fail = i
            answer[1] = (fail // n) + 1
            answer[0] = (fail % n) + 1
            break
        else:
            used.append(words[i])
            
        before = words[i]
    
    
    #print('fail:',fail)
    #print('used:',used)
    
    

    return answer
