def solution(participant, completion):
    answer = ''
    
    pDict = {}
    cDict = {}
    
    for p in participant:
        if not p in pDict:
            pDict[p] = 1
        else :
            pDict[p] += 1
    
    for c in completion:
        if not c in cDict:
            cDict[c] = 1
        else :
            cDict[c] += 1
            
    for key in pDict.keys():
        if not key in cDict:
            answer = key
            break
        if pDict[key] > cDict[key]:
            answer = key
            break
        
    return answer
