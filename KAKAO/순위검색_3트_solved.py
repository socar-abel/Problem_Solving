# 내가 도전한 문제중에 제일 오랫동안 고민하고 푼 문제.

# 1. 시간복잡도를 고려하며 문제풀이
# 2. 탐색이 필요한 경우 이진탐색 고려
# 3. case가 한정적으로 주어진 경우 (= 경우의 수가 상수인 경우)
# -> 아예 case 별로 테이블을 작성해버려 상수시간에 접근하는 것이 빠르다.

# Query 배열을 무조건 한 번씩은 순차탐색을 해야한다. O(Q)
# 순차탐색을 돌며 Query에 대한 info 탐색을 효율적으로 하는 것이 관건이다.
# Query로 나올 수 있는 경우의 수는 한정적이다 (108개). 이를 이용해야 한다.
# info를 순차 탐색하며 108개 경우의 수 집합에 분류하여 삽입한다.
# value(점수)로 dictionary를 sorting 한 뒤, binary search 알고리즘으로 수행시간을 최소화 한다.
# 점수는 parsing 한뒤 [-1] index로 pythonic하게 접근한다.

# bisect : 이진탐색 구현 신세계.
# bisect_left, bisect_right, count_by_range(a,left,right) 에 익숙해지자.

# 아래와 같이 replace를 2번이상 수행할 수 있다.
# query = query.replace(' and ',' ').replace('-','').split(' ')

# ''.join(list)를 이용해 list->string 형변환한다.

# 런타임 에러가 떴었는데, candidate가 null인 경우를 고려하지 않았기 때문이다.
# candidate = [] if not query in infoDict else infoDict[query] 으로 pythonic 한 코드 작성.


from itertools import combinations
from bisect import bisect_left

def solution(info, queries):
    answer = []
    infoDict = dict()

    for information in info:
        information = information.split(' ')
        
        for x in range(5):  # '-'가 0개 ~ 4개
            for combi in combinations(information[:-1], x):
                spec = ''.join(list(combi))
                
                if not spec in infoDict:
                    infoDict[spec] = [int(information[-1])]
                else:
                    infoDict[spec].append(int(information[-1]))
    
    for value in infoDict.values():     # 점수 이진탐색을 위한 sort
        value.sort()
    
    for query in queries:
        count = 0
        query = query.replace(' and ',' ').replace('-','').split(' ')
        cutLine = int(query[-1])
        query = ''.join(query[:-1])
        
        # query에 걸러 나온 후보 리스트. 여기서 이진탐색 수행.            
        candidate = [] if not query in infoDict else infoDict[query]     
        
        left = bisect_left(candidate,cutLine)
        #print(cutLine,left,candidate)
        
        if len(candidate) == 0:
            count = 0
        elif len(candidate) == 1:
            count = 1 if candidate[0] >= cutLine else 0
        else :
            count = len(candidate)-left
        
        answer.append(count)        
        
    return answer
