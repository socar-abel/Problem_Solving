# 무한 BFS 반복 연습
from collections import deque
n, m = 5, 6
graph = [
  [1,0,1,0,1,0],
  [1,1,1,1,1,1],
  [0,0,0,0,0,1],
  [1,1,1,1,1,1],
  [1,1,1,1,1,1]
]


def BFS(x1,y1):
  graph[x1][y1] = 1
  q = deque()
  q.append((x1,y1))
  
  while q:
    x, y = q.popleft()
    
    if x-1 in range(n) and graph[x-1][y] == 1:
      graph[x-1][y] = graph[x][y] + 1
      q.append((x-1,y))
    if x+1 in range(n) and graph[x+1][y] == 1:
      graph[x+1][y] = graph[x][y] + 1
      q.append((x+1,y))
    if y-1 in range(m) and graph[x][y-1] == 1:
      graph[x][y-1] = graph[x][y] + 1
      q.append((x,y-1))
    if y+1 in range(m) and graph[x][y+1] == 1:
      graph[x][y+1] = graph[x][y] + 1
      q.append((x,y+1))
    
    
BFS(0,0)
for a in range(n):
  for b in range(m):
    print(graph[a][b],end=' ')
  print()

print('답 : ',graph[n-1][m-1])

    
