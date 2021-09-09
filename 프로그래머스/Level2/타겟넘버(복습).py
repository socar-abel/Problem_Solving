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
