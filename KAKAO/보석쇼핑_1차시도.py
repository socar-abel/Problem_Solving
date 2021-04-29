# 이진탐색을 했는데도 효율성 실패라니 ;;

# 리스트 안에 모든 보석 종류를 가지고 있는지 판단
def haveAllGems(gems,kindOfGem,start,end):
    #print('start,end',start,end)
    mySet = set(gems[start:end+1])
    #print(mySet)
    if kindOfGem.issubset(mySet):
        #print('True')
        return True
    else : 
        #print('False')
        return False
    
# gems list에서 i번 부터 구매를 시작했을 때 가장 짧은 구간 [i:e] 구하기
# 이진 탐색 활용
def findIndex(gems,kindOfGem,i,start,end):
    result = 10001
    while start <= end:
        mid = (start+end) // 2
        # i 부터 mid 사이에 보석 종류가 다 있을 경우
        if haveAllGems(gems,kindOfGem,i,mid):
            if mid < result:
                result = mid
            end = mid - 1
        # i 부터 mid 사이에 보석 종류가 다 있지 않은 경우
        else :
            start = mid + 1
        #print('mid :',mid)
    if result == 10001:
        return -1
    else :
        return result
    
    
    

def solution(gems):
    answer = []
    # 보석 종류를 담은 집합
    gems.insert(0,gems[0])
    kindOfGem = set(gems)
    
    answer = [1,100000] # 1번 부터 100,000번 까지 구매
    for i in range(1,len(gems)):  # index i에서 구매 시작
        e = findIndex(gems,kindOfGem,i,i,len(gems)-1)
        if e == -1:
            pass
        else:
            tempList = [i,e]    # i번 부터 e번까지 구매
            # print(tempList,'까지 구매하면 모두 살 수 있습니다.')
            if (e-i) < (answer[1]-answer[0]):
                answer = tempList
        
    
    return answer
