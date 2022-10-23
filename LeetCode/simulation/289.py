class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), 
                     (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        m = len(board)
        n = len(board[0])
        
        new_board = [[0] * n for _ in range(m)]
        
        for x in range(m):
            for y in range(n):
                
                neighbors = 0
                
                for d in direction:
                    nx = x + d[0]
                    ny = y + d[1]
                    
                    if not ((0 <= nx < m) and (0 <= ny < n)):
                        continue
                    
                    if board[nx][ny] == 1:
                        neighbors += 1
                
                
                if board[x][y] == 1:
                    if neighbors == 2 or neighbors == 3:
                        new_board[x][y] = 1
                    else:
                        new_board[x][y] = 0
                else:
                    if neighbors == 3:
                        new_board[x][y] = 1
                    else:
                        new_board[x][y] = 0
        
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]
                        
                    
                
