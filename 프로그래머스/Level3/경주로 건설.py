from collections import deque
def solution(board):
    N = len(board)
    directions = [(-1,0), (0,-1), (1,0), (0,1)] # 상좌하우
    
    def bfs(x,y,cost,d): 
        graph = [[0]*N for _ in range(N)]
        for a in range(N):
            for b in range(N):
                if board[a][b] == 1 : graph[a][b] = -1  # 벽을 -1로 설정
        q = deque()
        q.append((x,y,cost,d))
        while q:
            x,y,cost,idx = q.popleft()
            for i in range(len(directions)):
                nx = x + directions[i][0]
                ny = y + directions[i][1]
                
                if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
                if graph[nx][ny] == -1 : continue

                if idx == i : newcost = cost + 100
                else : newcost = cost + 600
                
                if graph[nx][ny] == 0 or ((graph[nx][ny] != 0) and graph[nx][ny] > newcost):
                    q.append((nx,ny,newcost,i))
                    graph[nx][ny] = newcost
                    
                else : continue

        return graph[N-1][N-1]

    return min(bfs(0,0,0,2),bfs(0,0,0,3))
