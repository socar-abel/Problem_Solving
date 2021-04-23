from itertools import combinations

def solution(orders, course):
    answer = []
    # ordersCombi[0] = 크기 2인 조합들, [1] = 크기 3인 조합들
    ordersCombi = [[] for _ in range(len(course))]  
    
    for i in range(len(course)):
        for order in orders:        # "XYZ"
            order = list(order)     # "XYZ" to [X,Y,Z]
            order.sort()
            combiTupleList = list(combinations(order, course[i])) # [(X,Y),(X,X),..]
            for c in combiTupleList:
                if c not in ordersCombi[i]:
                    ordersCombi[i].append(c)
    print(ordersCombi)
            
    '''
    ordersCombi = [
        [('X', 'Y'), ('X', 'Z'), ('Y', 'Z'), ('W', 'X'), ('W', 'Y'), ('A', 'W'),                ('A','X')], 
        
        [('X', 'Y', 'Z'), ('W', 'X', 'Y'), ('A', 'W', 'X')], 
        
        []
    ]
    '''
    
    combiDict = dict()  # {XY:2, XZ:1, .. }   몇회 출현했는지
    
    for i in range(len(ordersCombi)):
        for oc in ordersCombi[i]:  # oc = ('X','Y')
            count = 0
            for order in orders:
                oc = set(oc)    # oc = {'X','Y'}
                order = list(order)
                order = set(order)  # order = {X,Y,Z}
                if oc.issubset(order):
                    count += 1
            oc = list(oc)
            oc.sort()
            oc = ''.join(oc)    # oc = "XY"
            combiDict[oc] = count     # oc : count
    
    print()
    print(combiDict)
    '''
    {'XY': 2, 'XZ': 1, 'YZ': 1, 'WX': 2, 'WY': 1, 'AW': 1, 'AX': 1, 'XYZ': 1,
        'WXY': 1, 'AWX': 1}
    '''
    # combiDict에서 value가 2이상이고, maxCount인 key를 answer에 담는다.
    # maxCount[0] = course[0] 크기 코스의 가장 많이 나온 횟수
    maxCount = [0]*len(course)  
    key_list = combiDict.keys()
    
    # maxCount 찾기
    for i in range(len(course)):
        for key in key_list:
            if course[i] == len(key) and combiDict[key] >= maxCount[i]:
                maxCount[i] = combiDict[key]
    
    print(maxCount) # [2, 1, 0]
    
    for i in range(len(course)):
        for key in key_list:
            # key의 길이가 course[i]와 같고, maxCount라면
            if course[i] == len(key) and maxCount[i] == combiDict[key] and maxCount[i]>=2:
                answer.append(key)
    answer.sort()
    
    
    return answer
