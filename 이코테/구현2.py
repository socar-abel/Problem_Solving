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
'''
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
