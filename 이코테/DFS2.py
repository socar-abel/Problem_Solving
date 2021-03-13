'''
# 5-8 DFS 예제
def dfs(graph,v,visited):
  print(v,end=' ')
  visited[v]=True
  for i in graph[v]:
    if not visited[i]:
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
  [1,7],
]

visited = [False]*9

dfs(graph,1,visited)
print()

# 5-9 BFS 예제
from collections import deque
def bfs(graph,start,visited):
  visited[start]=True 
  queue = deque([start])
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7],
]

visited = [False for _ in range(9)]

bfs(graph,1,visited)

# 3 음료수 얼려먹기 (순수 내가 짠 코드. 그러나 1,2는 왜 탐색하지 못할까)
# if와 elif의 관계로 짰기 때문이 아닐까? -> 완벽한 해결
n,m = map(int,input().split())
graph = [] 
for _ in range(n):
  graph.append(list(map(int,input())))

count=0

def bfs(graph,a,b):
  graph[a][b]=1
  print('[',a,b,']')
  # 상 하 좌 우
  if a-1 in range(n) and b in range(m) and graph[a-1][b] == 0:
    bfs(graph,a-1,b)
  if a+1 in range(n) and b in range(m) and graph[a+1][b] == 0:
    bfs(graph,a+1,b)
  if a in range(n) and b-1 in range(m) and graph[a][b-1] == 0:
    bfs(graph,a,b-1)
  if a in range(n) and b+1 in range(m) and graph[a][b+1] == 0:
    bfs(graph,a,b+1)

count = 0

for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      print(i,',',j,'에서 bfs 실행 !')
      count+=1
      bfs(graph,i,j)
      print()

print('count :',count)
'''

# 4 미로 탈출 
# bfs를 완벽하게 구현은 했지만 중간에 다른 곳으로 셀수 있어서 '최소' 칸은 구하지 못한다.
# 깨달음 : 큐에서 노드를 꺼낼때마다 count+=1을 하면 안된다 !
# 같은 계층 집합은 같은 level을 먹여야 한다.
from collections import deque 
n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input())))

# count = 0 이걸 하면 안됐었다.
move = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우
 
def bfs(graph,a,b):
  q=deque()
  q.append([a,b])
  graph[a][b]=0 # 첫 노드 방문처리 and level 1 부여. <<LOG1>>
  # global count 

  # 상하좌우 탐색 
  while q:
    v = q.popleft()
    # count += 1 # 꺼내는 순간 count ++
    x = v[0]
    y = v[1]
    # print('꺼낸 노드 :',x,y) 

    if x==n-1 and y==m-1 :
      break

    if x-1 in range(n) and not graph[x-1][y] == 0: # 방문하지 않은 인접 노드
      q.append([x-1,y]) # 큐에 넣고
      graph[x-1][y] = graph[x][y]+1 # 방문처리 and level 처리
    if x+1 in range(n) and not graph[x+1][y] == 0: # 방문하지 않은 인접 노드
      q.append([x+1,y]) # 큐에 넣고
      graph[x+1][y] = graph[x][y]+1 # 방문처리 and level 처리
    if y-1 in range(m) and not graph[x][y-1] == 0: # 방문하지 않은 인접 노드
      q.append([x,y-1]) # 큐에 넣고
      graph[x][y-1] = graph[x][y]+1 # 방문처리 and level 처리
    if y+1 in range(m) and not graph[x][y+1] == 0: # 방문하지 않은 인접 노드
      q.append([x,y+1]) # 큐에 넣고
      graph[x][y+1] = graph[x][y]+1 # 방문처리 and level 처리

bfs(graph,0,0)

# LOG1 에서 첫 노드를 1이 아닌 0으로 설정했기 때문에 +1.
# -> not 0으로 문법을 바꿈으로써 불편함 해결. 
print('최단거리 :',graph[n-1][m-1]) 
  


