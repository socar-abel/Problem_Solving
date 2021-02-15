'''
2021.02.14
DFS/BFS

# 5-1 스택 예제
# 파이썬에서 스택을 이용할 때는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작한다.
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()

stack.append(1)
stack.append(4)
stack.pop() 

print(stack)
print(stack[::-1])

# 5-2 큐 예제
# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용한다. deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다. 

from collections import deque

# 큐 (Queue)구현을 위해 deque 라이브러리 사용 
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() 
queue.append(1)
queue.append(4)
queue.popleft() 

print(queue)
queue.reverse() 
print(queue) 
print(list(queue)) # list(queue)를 하면 리스트 자료형으로 반환된다.


# 5-4 재귀함수 종료 예제
def recursive_function(i):
  # 10번째 출력했을 때 종료되도록 종료 조건 명시
  if i==10:
    return
  print(i,"번째 재귀함수에서",i+1,"번째 재귀 함수를 호출합니다.")
  recursive_function(i+1)
  print(i,"번째 재귀함수를 종료합니다.")

recursive_function(1)


# 5-5 2가지 방식으로 구현한 팩토리얼 예제
# 반복적으로 구현한 5!
result = 1
for i in range(1,6):
  result *= i 
print("5! =",result) 

# 재귀적으로 구현한 5!
def recursive(i):
  if i<=1 : return 1
  return i*recursive(i-1)

print("5! =",recursive(5))


# 5-6 인접 행렬 방식 예제
INF = 999999999 # 무한의 비용 선언
graph = [
  [0,7,5],
  [7,0,INF],
  [5,INF,0],
]

print(graph)

# 5-7 인접 리스트 방식 예제
graph2 = [[] for _ in range(3)] # vertex 수 만큼 생성
graph2[0].append((1,7))
graph2[0].append((2,5))

graph2[1].append((0,7))

graph2[2].append((0,5))

print(graph2)


# 5-8 DFS 예제
# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
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

visited=[False]*9
dfs(graph,1,visited)

# 5-9 BFS 예제
from collections import deque

# BFS 메서드 정의
def bfs(graph,start,visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft() 
    print(v, end = ' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
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

visited=[False]*9
bfs(graph,1,visited)
print()


# 3 음료수 얼려 먹기 
# 혼자 진짜 못풀겠음. 밑에는 망한 내 코드.

def makeGraph(arr,n,m):
  graph = [[]*m for _ in range(n)]
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      # 상
      if i-1 in range(n):
        graph[i][j].append([i-1][j])
      # 하
      if i+1 in range(n):
        print("log",i+1)
        graph[i][j].append([i+1][j])
      # 좌
      if j-1 in range(m):
        graph[i][j].append([i][j-1])
      # 우
      if j+1 in range(m):
        graph[i][j].append([i][j+1])
  return graph

def dfs(graph, i, j, visited):
  visited[i][j]=True
  print(i,j,end=' ')
  for i in graph[i][j]:
    if not visited[i][j]:
      dfs(graph,i,visited)

n,m=map(int,input().split())
array = []
for i in range(n):
  array.append(list(map(int,input().split())))


 
graph = makeGraph(array,n,m)

visited=[[False]*m for _ in range(n)]
count = 0

for i in range(graph):
  for j in range(graph[i]):
    if not graph[i][j]==1 and not visited[i][j]:
      dfs(graph,i,j,visited)

print("count :",count)



# 책의 풀이
# N,M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<=-1 or x>=n or y<=-1 or y>=m:
    print(x,y,'범위 이탈입니다.')
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    print("(",x,",",y,")",'방문했습니다.')
    graph[x][y] = 1
    # 상, 하, 좌, 우의 위치도 모두 재귀 적으로 호출
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    print(x,y,'상하좌우 모두 끝났습니다. return True')
    return True
  
  print(x,y,'if문에 걸러지지 않고 리턴합니다. return False')
  return False

print()
print('for문 시작합니다.')
result=0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    print()
    print(i,j,"<dfs 시작>")
    check=dfs(i,j)
    print('dfs',i,j,'결과 :',check)
    print()
    if check == True:
      result+=1
      print("result + 1 =",result)

print("결과 :",result)

'''

# 4 미로탈출 
from collections import deque

# N,M을 공백으로 구분하여 입력받기
n, m = map(int , input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 이동할 네 방향의 정의 (상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if graph[nx][ny]==0:
        continue 
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] +1
        queue.append((nx,ny))
  return graph[n-1][m-1]

print('결과 :',bfs(0,0))
