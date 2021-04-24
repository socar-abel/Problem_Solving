'''
def dfs(graph,start,visited):
  visited[start] = True
  print(start,end=' ')
  for v in graph[start]:
    if not visited[v]:
      dfs(graph,v,visited)

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

dfs(graph,1,visited)
print()


from collections import deque 

def bfs(graph,start,visited):
  q = deque()
  q.append(start)
  visited[start] = True
  print(start, end=' ')
  while q:
    i = q.popleft() 
    for node in graph[i]:
      if not visited[node]:
        q.append(node)
        visited[node] = True
        print(node, end=' ')


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

bfs(graph,1,visited)
print()
'''
