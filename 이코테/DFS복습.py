"""
# 5-6 인접 행렬 방식 예제
INF = 987654321
graph = [
  [0,7,5],
  [7,0,INF],
  [5,INF,0]
]

print(graph)


# 5-7 인접 리스트 방식 예제
graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))

print(graph)

# 5-8 DFS 예제
def dfs(graph, v, visited):
  visited[v]=True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:  # 이 조건 잊지 말기 
      dfs(graph,i,visited)

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,8]
]

visited = [False]*9

dfs(graph, 1, visited)
print()


# 5-9 BFS 예제
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start]=True
  
  while queue:
    v = queue.popleft() 
    print(v, end = ' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9

bfs(graph, 1, visited)
print()


# 3 음료수 얼려먹기

n,m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int,input())))

def dfs(x,y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    print(x,y,": 범위를 벗어납니다.")
    return False
  if not graph[x][y] == 1:
    graph[x][y] = 1

    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    print("상하좌우 수행 완료했습니다.")
    return True
  return False

count = 0

for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      count+=1

print("얼려진 음료수의 개수 :",count)

"""

# 4 미로 탈출
from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input()))) # 이거 꼭 list 붙여줘야 함.

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:      
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx <=-1 or nx >= n or ny <= -1 or ny >= m:
        continue
      if graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  return graph[n-1][m-1]

print(bfs(0,0))
