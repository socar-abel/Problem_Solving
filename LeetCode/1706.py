class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        answer = [-1] * n
        
        for column in range(n):
            position = [-1, column]
            
            for i in range(m):
                nx = i
                y = position[1]
                grid_direction = grid[nx][y]
                
                if grid_direction == 1:
                    ny = position[1] + 1
                    
                    # 벽에 닿는다면
                    if ny > n - 1:
                        break
                        
                    # 갇힌다면
                    if grid[nx][ny] == -1:
                        break
                        
                else:
                    ny = position[1] - 1
                
                    # 벽에 닿는다면
                    if ny < 0:
                        break
                    
                    # 갇힌다면
                    if grid[nx][ny] == 1:
                        break
                
                position = [nx, ny]
            
                if i == m-1:
                    answer[column] = ny
        
        return answer
