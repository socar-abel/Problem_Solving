class Solution:
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 우 하 좌 상
        answer = [[0] * n for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        new_matrix = [(0, 0)]
        x = 0
        y = 0
        d = 0
        
        for _ in range(n**2 - 1):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            
            if 0 <= nx < n and 0 <= ny < n and ( (nx, ny) not in new_matrix ):
                new_matrix.append((nx, ny))
            else:
                d = (d + 1) % 4
                nx = x + direction[d][0]
                ny = y + direction[d][1]
                new_matrix.append((nx, ny))
                
            x = nx
            y = ny

        print(new_matrix)
        
        num = 1
        for i, j in new_matrix:
            answer[i][j] = num
            num += 1
        
        return answer
        
