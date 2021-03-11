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


