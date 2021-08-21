def rotate(puzzle): # 90도 회전
    xlen = len(puzzle); ylen = len(puzzle[0])
    rotate_puzzle = [[-1]*(xlen) for _ in range(ylen)]
    for a in range(ylen):
        for b in range(xlen):
            rotate_puzzle[a][b] = puzzle[xlen-1-b][a]
    
    return rotate_puzzle

def solution(board, table):
    answer = 0; N = len(board)
    blanks = []; puzzles = [];
    visited = [[False]*N for _ in range(N)]
    visited2 = [[False]*N for _ in range(N)]
    
    def DFS(x,y,blank): # DFS for game_board
        visited[x][y] = True
        blank.append((x,y))
        # 상하좌우
        if x-1 in range(N) and board[x-1][y] == 0 and not visited[x-1][y]: DFS(x-1,y,blank)
        if x+1 in range(N) and board[x+1][y] == 0 and not visited[x+1][y]: DFS(x+1,y,blank)
        if y-1 in range(N) and board[x][y-1] == 0 and not visited[x][y-1]: DFS(x,y-1,blank)
        if y+1 in range(N) and board[x][y+1] == 0 and not visited[x][y+1]: DFS(x,y+1,blank)
    
    def DFS2(x,y,puzzle): # DFS2 for table
        visited2[x][y] = True
        puzzle.append((x,y))
        # 상하좌우
        if x-1 in range(N) and table[x-1][y] == 1 and not visited2[x-1][y]: DFS2(x-1,y,puzzle)
        if x+1 in range(N) and table[x+1][y] == 1 and not visited2[x+1][y]: DFS2(x+1,y,puzzle)
        if y-1 in range(N) and table[x][y-1] == 1 and not visited2[x][y-1]: DFS2(x,y-1,puzzle)
        if y+1 in range(N) and table[x][y+1] == 1 and not visited2[x][y+1]: DFS2(x,y+1,puzzle)
    
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0 and not visited[x][y]:
                tempBlank = []
                DFS(x,y,tempBlank)
                blanks.append(tempBlank)
                
    for x in range(N):
        for y in range(N):
            if table[x][y] == 1 and not visited2[x][y]:
                tempPuzzle = []
                DFS2(x,y,tempPuzzle)
                puzzles.append(tempPuzzle)

    # formalize 
    formal_blanks = []; formal_puzzles = []
    
    for blank in blanks:
        x1, y1 = min(blank, key = lambda x : x[0])[0], min(blank, key = lambda x : x[1])[1]
        x2, y2 = max(blank, key = lambda x : x[0])[0], max(blank, key = lambda x : x[1])[1]
        formal_blank = [[-1]*(y2-y1+1) for _ in range(x2-x1+1)]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if (i,j) in blank : formal_blank[i-x1][j-y1] = 1
                else : formal_blank[i-x1][j-y1] = 0
        formal_blanks.append(formal_blank)
    
    for puzzle in puzzles:
        x1, y1 = min(puzzle, key = lambda x : x[0])[0], min(puzzle, key = lambda x : x[1])[1]
        x2, y2 = max(puzzle, key = lambda x : x[0])[0], max(puzzle, key = lambda x : x[1])[1]
        formal_puzzle = [[-1]*(y2-y1+1) for _ in range(x2-x1+1)]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if (i,j) in puzzle : formal_puzzle[i-x1][j-y1] = 1
                else : formal_puzzle[i-x1][j-y1] = 0
        formal_puzzles.append(formal_puzzle)
    
    # formal_puzzles + their rotated_puzzles
    all_formal_puzzles = []
    for fpuzzle in formal_puzzles:
        puzzle_set = []
        puzzle_set.append(fpuzzle)
        for _ in range(3):
            fpuzzle = rotate(fpuzzle)
            puzzle_set.append(fpuzzle)
        all_formal_puzzles.append(puzzle_set)
    
    # preventing double counting   
    used_puzzle_set = [False]*len(all_formal_puzzles)
    match = []  # Finalized Puzzles
    
    # Comparing the blanks with the puzzles
    for formal_blank in formal_blanks:
        stop = False
        for i in range(len(all_formal_puzzles)):
            puzzle_set = all_formal_puzzles[i]
            for puzzle in puzzle_set:
                if formal_blank == puzzle and not used_puzzle_set[i]:
                    match.append(formal_blank); used_puzzle_set[i] = True; stop =True
                    break
            if stop : break
            
    # counting the number of blocks
    for shape in match:
        block = 0
        for x in range(len(shape)):
            for y in range(len(shape[0])):
                if shape[x][y] == 1 : block += 1
        answer += block
        
    return answer
