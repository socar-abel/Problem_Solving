'''
## 예제 4-1 상하좌우
# 나의 풀이
n = int(input())
move = input().split()
x=1
y=1

print(move)

for i in move:
  if i == "L":
    if(y-1 in range(1,6)):
      y-=1
  if i == "R":
    if(y+1 in range(1,6)):
      y+=1
  if i == "U":
    if(x-1 in range(1,6)):
      x-=1
  if i == "D":
    if(x+1 in range(1,6)):
      x+=1

print(x,y)

# 책의 풀이
n = int(input())
x,y=1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x+dx[i]
      ny = y+dy[i]
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  x,y = nx, ny
print(x,y)


N = int(input())
count = 0

for h in range(N+1):
  for m in range(60):
    for s in range(60):
      time = str(h)+str(m)+str(s)
      if "3" in time:
        count+=1
      
print(count)


## 2 왕실의 나이트
# 나의 답안
x = input() 
print(x)
col = x[0]
row = x[1]

cols = ['a','b','c','d','e','f','g','h']
count = 0

# 상,하,좌,우
if int(row)-2 in range(1,9):
  if cols[cols.index(col)-1] in cols:
    count+=1
    print(1)
  if cols[cols.index(col)+1] in cols:
    count+=1
    print(2)
if int(row)+2  in range(1,9):
  if cols.index(col)-1 in range(8):
    count+=1
    print(3)
  if cols.index(col)+1 in range(8):
    count+=1
    print(4)
if cols.index(col)-2 in range(8):
  if int(row)-1 in range(1,9):
    count+=1
    print(5)
  if int(row)+1 in range(1,9):
    count+=1
    print(6)
if cols.index(col)+2 in range(8): 
  if int(row)-1 in range(1,9):
    count+=1
    print(7)
  if int(row)+1 in range(1,9):
    count+=1
    print(8)
print("총"+count+" 가지")


# 책의 답안. 훨씬 간결하다.
input_data = input() 
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if 1<=next_row<=8 and 1<=next_column<=8:
    result+=1
print(result)

금요일 저녁~ 토요일 새벽.


## 3 게임 개발. 처음으로 책의 코드보다 내 코드가 더 간결했던 문제.
# 나의 코드
# 방문을 했다면 2로 만들어 버린다.
n, m = map(int,input().split())
x, y, direction = map(int,input().split())

maps = []
for i in range(n):
  maps.append(list(map(int,input().split())))

directrions = ['N','E','S','W']
moves = [(-1,0),(0,1),(1,0),(0,-1)] # 북 동 남 서

count = 1
def go(x, y, d):
  maps[x][y]=2 # 시작 노드 방문
  print(x,y,"방문")
  direction = 0 
  global count  
  for _ in range(4): # 4 방향 탐색
    nextX = x + moves[d][0]
    nextY = y + moves[d][1]
    # print(nextX, nextY)
    # 0 인 곳은 방문하러 감
    if nextX in range(n) and nextY in range(m) and maps[nextX][nextY] == 0:     
      count += 1
      maps[nextX][nextY] = 2
      go(nextX,nextY,d)
    elif nextX in range(n) and nextY in range(m) and maps[nextX][nextY] == 2:
      pass
    else:
      pass
    d-=1  
    if d<-4 : d = -1
    if d>3 : d = 0 # 이 코드는 없어도 되는 코드였다.
    direction+=1
  # 4 방향 모두 탐색했고, 뒤로 갈 곳이 바다 일 때 함수 종료
  if(direction==4 and maps[nextX][nextY]==1): return  

go(x,y,direction)
print("count :",count)
'''

# 책의 코드
n,m = map(int,input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]

# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x,y,direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
  array.append(list(map(int,input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -=1
  if direction == -1:
    direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
  #왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time+=1
  if turn_time==4:
    nx = x-dx[direction]
    ny = y-dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else: 
      break
    turn_time = 0
print(count)
