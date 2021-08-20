def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def DFS(x):
        visited[x] = True
        for i in range(len(computers[x])):
            if x != i and computers[x][i] == 1 and visited[i] == False:
                DFS(i)
    
    for x in range(len(computers)):
        if visited[x] == False : DFS(x); answer += 1
    
    
    return answer
