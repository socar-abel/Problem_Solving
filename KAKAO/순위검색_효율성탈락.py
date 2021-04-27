# 파싱을 하면 string형이 되므로 int(pq[i])를 해줬어야 했다.
# 효율성 틀림..
# 배운 스킬 1 : replace(" and "," ").split(" ")
# 배운 스킬 2 : c = sorted(a, key=lambda x : x[0])
# I = 50,000 
# Q = 100,000
def solution(info, query):
    answer = []
    
    parsedQ = []
    parsedI = []
    
    for q in query :    # q = "java and backend and .."
        # q 파싱
        # parsedQ = [ [java, backend, ..], ['pyhthon, frontend..'], .. ] 
        # parsedQ = [temp, temp, temp]
        temp = (q.split(' and '))        
        temp.append(temp[3].split(' ')[0])
        temp.append(temp[3].split(' ')[1])
        del temp[3]
        parsedQ.append(temp)
        
    print('========parsedQ========')
    print(parsedQ)
    
    for i in info : # i = "java backend junior .."
            # i 파싱
            # paredI = [ ['java', 'backend',..], ['python', 'frontend',], ..]
            parsedI.append(i.split(' '))
            
    print('========parsedI========')
    print(parsedI)
        
    # answer 구하기
    for pq in parsedQ:
        count = 0
        for pi in parsedI:
            if ( (pq[0] == pi[0]) or pq[0] == '-') and ( (pq[1] == pi[1]) or pq[1] == '-') and ( (pq[2] == pi[2]) or pq[2] == '-') and ( (pq[3] == pi[3]) or pq[3] =='-') and int(pq[4]) <= int(pi[4]):
                
                count += 1
        answer.append(count)
    
    return answer
