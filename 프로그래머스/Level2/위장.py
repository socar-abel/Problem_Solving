def solution(clothes):
    answer = 1
    dic = dict()
    
    for cloth in clothes:
        if not cloth[1] in dic:
            dic[cloth[1]] = [cloth[0]]
        else : dic[cloth[1]].append(cloth[0])
    
    print(dic)
    for key in dic.keys():
        answer *= (len(dic[key])+1)
    
    return answer-1
