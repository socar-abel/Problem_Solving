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
'''

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
