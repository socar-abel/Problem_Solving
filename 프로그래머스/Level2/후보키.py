from itertools import combinations

def solution(relation):
    answer = 0
    attriNum = len(relation[0]) 
    candidates = []
    students = []
    
    for r in relation:
        student = dict()
        for i in range(attriNum):
            student[i] = r[i]
        
        students.append(student)
        
    attributes = [x for x in range(attriNum)]
    attriCombi = [] # ([0,1,2,...(0,1),(0,2)]
    
    for i in range(1,attriNum+1):
        c = list(combinations(attributes, i))
        attriCombi.append(c)
    
    #print(attriCombi)
    for combiList in attriCombi:
        for combi in combiList:
            #print('combi',combi)
            checkList = []
            for s in students:
                tempList = []
                for c in combi:
                    tempList.append(s[c])
                checkList.append(tuple(tempList))
            #print('checkList',checkList)
            if len(checkList) == len(set(checkList)) : candidates.append(combi)
    
    #print()
    #print('candidates',candidates)
    
    remove = []
    
    for candidate in candidates:
        for other in candidates:
            if set(candidate).issubset(other) and candidate != other:
                remove.append(other)
        
    #print('remove',remove)
    
    candidates = [x for x in candidates if x not in remove]
    #print(candidates)
    
    return len(candidates)
