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

"""

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
