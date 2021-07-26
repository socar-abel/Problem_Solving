from itertools import combinations

def solution(clothes):
    answer = 0
    spyDict = dict()
    
    for x in clothes:
        if not x[1] in spyDict:
            spyDict[x[1]] = [x[0]]
        else : spyDict[x[1]].append(x[0])
    
    typeCombi = []
    for i in range(1,len(spyDict.keys())+1):
        c = list(combinations(spyDict.keys(),i))
        typeCombi.append(c)
    
    for combiList in typeCombi:
        print('combiList',combiList)
        for combi in combiList:
            print('combi',combi)
            temp = 1
            for kind in combi:
                print('type',kind)
                print('len',len(spyDict[kind]))
                temp *= len(spyDict[kind])
            answer += temp
    
    return answer
