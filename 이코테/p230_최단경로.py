'''
# 9-1 간단한 다익스트라 알고리즘 소스코드
import sys 
input = sys.stdin.readline
INF=int(1e9)
# n : 노드의 개수, m : 간선의 개수
n, m = map(int, input().split())
# 다익스트라를 시작할 노드
start = int(input())
# 인접 리스트 기반의 그래프
graph = [[] for i in range(n+1)]
# 방문 기록 리스트
visited = [False]*(n+1)
# 최단거리 테이블
distance = [INF]*(n+1)

# 간선 정보 입력받기
for _ in range(m):
  # a번 노드는 b번 노드와 연결되어 있고, 간선의 길이는 c 이다.
  a,b,c, = map(int, input().split())
  graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 시작 노드로부터 가장 최단거리가 짧은 노드의 번호를 반환. (최단거리 테이블에서 찾는다.)
def get_smallest_node():
  min_value = INF 
  index = 0
  # 가장 최단거리인 노드 찾기. 이 for문을 지나면 찾을 수 있다.
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

# 다익스트라 알고리즘
def dijkstra(start):
  # 시작노드에 대해서 초기화 작업
  distance[start] = 0
  visited[start] = True
  # start와 이어진 노드들에 대하여. j = (b,c)
  for j in graph[start]:
    distance[j[0]] = j[1]

  # 시작 노드를 제외한 전체 n-1개의 노드에 대해 본격적으로 알고리즘 반복
  for i in range(n-1): # 굳이 i 가 아닌 _로 설정해도 될 것 같다.
    now = get_smallest_node() 
    visited[now] = True
    # 현재 노드와 연결된 다른 노드들을 확인한다.
    for j in graph[now]:
      cost = distance[now]+j[1] 
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost  

dijkstra(start)

print(distance)


# 복습
# 9-1 간단한 다익스트라 알고리즘 소스코드
import sys 
input = sys.stdin.readline 
INF = int(1e9)

n, m = map(int, input().split())
start = int(input()) 
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[]for i in range(n+1)]
# 방문한 적이 있는지 체그하는 목적의 리스트 만들기
visited = [False]*(n+1)
distance = [INF]*(n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
  
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    # j[0] = b, j[1] = c
    distance[j[0]] = j[1]

  # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
  for i in range(n-1):
    now = get_smallest_node() 
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]

      if cost < distance[j[0]]:
        distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else : 
    print(distance[i])


# 9-2 개선된 다익스트라 알고리즘 소스코드
import heapq
import sys 
input = sys.stdin.readline 
INF = int(1e9) 

n,m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  # 시작 노드로 가기 위한 최단 경로는 0 으로 설정하여, 큐에 삽입
  q = [] 
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q: # 큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else : 
    print(distance[i])



# 9-3 플로이드 워셜 알고리즘 소스코드
INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든값을 무한 으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화 
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a, b, c = map(int, input().split())
  graph[a][b] = c
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b]) 
# 수행된 결과를 출력
for a in range(1,n+1):
  for b in range(1,n+1):
    # 도달할 수 없는 경우, INFINITY 라고 출력
    if graph[a][b]==INF:
      print("INFINITY",end=' ')
    else:
      print(graph[a][b],end=' ')
  print()


# (복습) 9-3 플로이드 워셜 알고리즘
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트 (그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b]=0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정 
  a, b, c = map(int,input().split())
  graph[a][b]=c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if graph[a][b] == INF:
      print("INFINITY",end = ' ')
    else:
      print(graph[a][b],end=' ')
  print()


# 2 미래 도시 
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int,input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
  a,b = map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

# 거처 갈 노드 X와 최종 목적지 노드 K를 입력받기
x,k = map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k]+graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
  print("-1")
else:
  print('distance :',distance)


'''

# 3 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist+i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
  if d!=INF :
    count+=1
    max_distance = max(max_distance,d)

print(count-1,max_distance)


