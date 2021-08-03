# 플로이드 워셜 알고리즘
# O(N^3) time

INF = 987654321 
n, m = 4, 7 
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1): 
  graph[a][a] = 0 

graph[1][2] = 4; graph[1][4] = 6
graph[2][1] = 3; graph[2][3] = 7
graph[3][1] = 5; graph[3][4] = 4
graph[4][3] = 2

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    print(graph[a][b], end=' ')
  print()

