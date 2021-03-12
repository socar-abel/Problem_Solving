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
'''
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
 
