# DFS 알고리즘을 이용한다는 생각이 죽어도 안떠올랐었는데, 이젠 자연스레 떠올라서 해결하였다.
answer = 0
def solution(numbers, target):

    def dfs(i, result):
        global answer
        if i == len(numbers):
            if result == target : answer += 1
            return
            
        dfs(i+1, result + numbers[i])
        dfs(i+1, result - numbers[i])
    
    dfs(0,0)
    
    return answer
