# p257 플로이드 워셜 알고리즘 소스코드
INF = 123456789

n = 4
m = 7
# 최단거리 테이블
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b] = 0

graph[1][2] = 4
graph[1][4] = 6
graph[2][1] = 3
graph[2][3] = 7
graph[3][1] = 5
graph[3][4] = 4
graph[4][3] = 2

for v in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][v]+graph[v][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print("INF",end=' ')
    else:
      print(graph[a][b],end=' ')
  print()
