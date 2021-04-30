# 무한 DFS 반복연습

n, m = 5, 5
graph = [
  [0,0,1,1,0],
  [0,0,0,1,1],
  [1,1,1,1,1],
  [0,1,0,0,0],
  [0,0,1,1,1]
]

def DFS(x,y):
  if graph[x][y] == 0:
    graph[x][y] = 1
  # 상하좌우
  if x-1 in range(n) and graph[x-1][y] == 0 :
    DFS(x-1,y)
  if x+1 in range(n) and graph[x+1][y] == 0 :
    DFS(x+1,y)
  if y-1 in range(m) and graph[x][y-1] == 0 :
    DFS(x,y-1)
  if y+1 in range(m) and graph[x][y+1] == 0 :
    DFS(x,y+1)

count = 0

for a in range(n):
  for b in range(m):
    if graph[a][b] == 0:
      print(a,b)
      count += 1
      DFS(a,b)

print('음료 개수:',count)
