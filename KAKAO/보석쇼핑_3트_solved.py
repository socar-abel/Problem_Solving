# 투 포인터 사용 - 효율성 1개 통과함 ㅋㅋ
# set(tempSum) : deque -> set 형변환 할 때 O(N)이 소요되었던 것 같다.

# 왜 list, set, deque을 사용할 생각만 했을까?
# dictionary에 {DIA : 4, RUBY : 2, EMERALD : 1, SAPPHIRE : 1}
# 이렇게 담아도 되는 것이었다.
# 중복된 원소 처리에 있어서 set만을 고집 했던 것 같다.

# 투 포인터 알고리즘 사용에는 문제가 없었다. O(N)이 소요되기 때문이다.

# dictionary에서 get 함수 사용을 익히자.

from collections import deque

def solution(gems):
    answer = [0,len(gems)]
    
    kindOfgems = len(set(gems)) # O(n)
    start = 0
    end = 0
    
    tempSum = dict()
    for start in range(len(gems)):
        #print('start:',start)
        while len(tempSum) < kindOfgems and end < len(gems):
            # DIA를 뽑았을 때 이전에 없었다면 0, 있었다면 거기에 1 추가.
            tempSum[gems[end]] = tempSum.get(gems[end],0) + 1 
            #print('end:',end,'tempSum:',tempSum)
            
            end +=1 
                    
        if len(tempSum) == kindOfgems:
            if end - (start+1) < (answer[1]-answer[0]): 
                answer=[start+1,end]
            elif end - (start+1) == (answer[1]-answer[0]): 
                if start+1 < answer[0]:
                    answer = [start+1,end]
                else:
                    pass
        
        
        if tempSum[gems[start]] == 1:
            del tempSum[gems[start]]
        else :
            tempSum[gems[start]] -= 1
        #print('뺀 후',tempSum)
            
    
    
    return answer
