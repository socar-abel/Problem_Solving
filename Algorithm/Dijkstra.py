# p248 개선된 다익스트라 알고리즘 소스코드
# 파이썬의 heapq 라이브러리는 원소로 튜플을 입력받으면
# 튜플의 첫 번째 원소를 기준으로 우선순위 큐를 구성한다.
# 따라서 (거리, 노드번호) 순서대로 튜플 데이터를 구성하는 것이 좋다.
import heapq
import sys
input = sys.stdin.readline
INF = 123456789

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
edge = [
  [1,2,2],[1,3,5],[1,4,1],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],
  [4,5,1],[5,3,1],[5,6,2]
]
distance = [INF]*(n+1)

for e in edge:
  a, b, c = e[0], e[1], e[2]
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)

    # 이미 처리된 노드 거르기
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
