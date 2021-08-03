# 개선된 다익스트라 알고리즘
# O(ElogV) time
import heapq

INF = 987654321
graph = [[],
[(2,2),(3,5),(4,1)],
[(3,3),(4,2)],
[(2,3),(6,5)],
[(3,3),(5,1)],
[(3,1),(6,2)],
[]
]
n, start = 6, 1
distance = [INF] * (n+1)

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q) 
    if distance[now] < dist:
      continue  
    for i in graph[now]:
      cost = dist + i[1]  
      if cost < distance[i[0]]:
        distance[i[0]] = cost  
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print('INF', end=' ')
  else : print(distance[i], end= ' ')
print()
  
