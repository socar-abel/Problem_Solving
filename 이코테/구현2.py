'''
# 예제 4-1 상하좌우 ((이거 tmp1, tmp2가 왜 서로 다르게 나오는 거지 ??))
# 파이썬에서는 얕은 복사, 깊은 복사가 일어난다고 함. 아직은 잘 모르겠음..
n = int(input())
commands = list(input().split()) 

moves = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
location = [1,1]

for command in commands: 
  tmp = location
  print('tmp1:',tmp)

  if command == "U":
    location[0] += moves[0][0]
    location[1] += moves[0][1]
    print('U')
    print(location)
  elif command == "D":
    location[0] += moves[1][0]
    location[1] += moves[1][1]
    print('D')
    print(location)
  elif command == "L":
    location[0] += moves[2][0]
    location[1] += moves[2][1]
    print('L')
    print(location)
  elif command == "R":
    location[0] += moves[3][0]
    location[1] += moves[3][1]
    print('R')
    print(location)

  print('tmp2:',tmp)
  if not( 1<=location[0]<=n and 1<=location[1]<=n ):
    print('error tmp:',tmp)
    location = tmp 
    print('error',location)
    print()

print('result:',location)

# 4-1 책의 코드 
n = int(input())
x, y = 1, 1
plans = input().split()

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
move_types=['U','D','L','R']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx<1 or ny <1 or nx>n or ny>n:
    continue
  x, y = nx, ny

print(x,y)

# 예제 4-2 시각. 나의 코드와 책의 코드가 일치함 !
n = int(input())

count = 0

for h in range(n+1):
  for m in range(60):
    for s in range(60):
      hour = str(h)+str(m)+str(s)
      if '3' in hour:
        count+=1

print('count :',count)

# 2 왕실의 나이트 
input = input() # input 보다는 input_data 라고 이름 붙이는 것이 더 좋다.
case = 0 

location = [ord(input[0])-ord("a")+1,int(input[1])]
print(location)
moves = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

for move in moves:
  next = [location[0]+move[0], location[1]+move[1]]
  if next[0] < 1 or next[1] < 1 or next[0] > 8 or next[1] >8:
    continue
  case+=1 

print(case)


# 3 게임 개발 (실패한 코드)
n, m = map(int,input().split())
x, y, d = map(int,input().split())

graph = []

for _ in range(n):
  input_list = list(map(int,input().split()))
  graph.append(input_list)

directions = [(-1,0),(0,1),(1,0),(-1,0)] # 북 동 남 서 
count = 0

check=0
while True:
  
  if check==4:
    nx, ny = x-directions[d][0], y-directions[d][1]
    check=0
    if graph[nx][ny] == 1 :
      break

  d-=1
  if d < -4:
    d = -1

  nx, ny = x+directions[d][0] , y+directions[d][1] 
  
  if graph[x][y] == 0 :
    x, y = nx, ny  
    graph[x][y]=2
    count+=1 
  else : 
    check+=1



print(count)
'''

# 3 게임 개발. 무한루프에 빠져버림. 결국 해결함,,
n,m = map(int,input().split())
x,y,d = map(int,input().split())
graph = []

for _ in range(n):
  graph.append(list( map( int,input().split() ) ))

direction = [(-1,0),(0,1),(1,0),(0,-1)] # 북 동 남 서 

graph[x][y]=2 # 시작 노드 방문처리
count = 1
check = 0


while True:
  print('- 현재위치 :',x,',',y)
  d-=1
  if d==-1:
      d=3
  nx = x+direction[d][0]
  ny = y+direction[d][1]
  print('d =',d)
  print('nx, ny :',nx,ny)     

  if graph[nx][ny] == 0:
    graph[nx][ny] = 2 # 방문처리
    x = nx
    y = ny 
    count += 1
    check = 0
    print('방문, count+=1')
  else:
    check += 1
    print('회전, check+=1')
    print('check :',check)
    

  if check >= 4 :
    print('현재 d :',d)
    x = x-direction[d][0]
    y = y-direction[d][1]
    print('뒤로 후퇴') 
    print('뒤로가면,',x,',',y)
    
    if graph[x][y] == 1:
      break
    else:
      check=0

print('result :',count)
