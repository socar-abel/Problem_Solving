# 사전 자료형으로 짜는게 더 예쁜듯.
# 파이썬 자료형(data type) 공부가 아직 부족함을 느낌.
# 파이썬의 Dictionary 자료형은 내부적으로 해시 테이블을 이용한다.
# 따라서 데이터의 탐색(검색) 및 수정이 O(1)에 처리된다.
# 근데 어차피 count = []에서도 O(I) 만큼 탐색을 해서 그런지 효율성 실패.

# Info = 50,000, Query = 100,000 크기 

def solution(info, query):
    answer = []
    
    infoDict = []       # [ {지원자A정보}, {지원자B정보}, ..]
    for i in info:
        i = i.split(' ')    # parsing
        data = dict()
        data['language'] = i[0]
        data['job'] = i[1]
        data['career'] = i[2]
        data['food'] = i[3]
        data['score'] = int(i[4])
        infoDict.append(data)
        
    #print('infoDict :',infoDict)
        
    for q in query:     # [ [q], [q], ..]
        q = q.replace(' and ', ' ').split(' ')
        #print('q : ',q)
        count = [ data for data in infoDict 
                 if (data['language'] == q[0] or q[0] == '-') and
                    (data['job'] == q[1] or q[1] == '-') and
                    (data['career'] == q[2] or q[2] == '-') and
                    (data['food'] == q[3] or q[3] == '-') and
                    data['score'] >= int(q[4]) ]
        #print('count : ',count)
        answer.append(len(count)) 
        
    
    return answer
