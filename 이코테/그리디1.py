'''
2021.02.12 서진이랑 까치산 스벅

## 예제 3-1 거스름 돈
# 내가 짠 코드 
n = 2580
coins = 0
a=0 #500, 100, 50, 10
b=0
c=0
d=0

while(True):
  a+=1
  if(500*a>n):
    a-=1
    break 
  
coins+=a
n = n%500

while(True):
  b+=1
  if(100*b>n):
    b-=1
    break 
  
coins+=b
n = n%100

while(True):
  c+=1
  if(50*c>n):
    c-=1
    break 
  
coins+=c
n = n%50

while(True):
  d+=1
  if(10*d>n):
    d-=1
    break 
  
coins+=d
n = n%10

print("동전 개수 :",a,b,c,d," ",coins)

# 책의 코드. 훨씬 간결함.
n = 2580
count = 0
coin_types = [500,100,50,10]
for coin in coin_types:
  count += n //coin
  n %= coin
print(count)

## 2 큰 수의 법칙
# 풀이 1: 그리디 알고리즘
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for _ in range(k):
    result+=first
    m-=1
    if m==0:
      break
  
  result+=second
  m-=1
  if m==0 :
    break
  
print(result)

# 풀이 2: 문제를 이해한 뒤, 공식을 만들어서 풀기
n = 5
m = 8
k = 3

data = [2,4,5,4,6]

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

result = (m//(k+1))*(k*first + second) + (m%(k+1))*(first)
print("공식으로 낸 답 :",result)



## 3 숫자 카드 게임 
# 내 답안
n,m = map(int,input().split())
array = [[0]*m for _ in range(n)]

for i in range(n):
  array[i] = list(map(int,input().split()))

result = 0

for i in range(n):
  if i==0:
    result = min(array[i])
  else:
    if(min(array[i])>=result):
      result = min(array[i])

print("카드 최소값 :",result)

# 책의 답안에서는 result = max(result,min_value) 문법을 이용했다.
'''


## 1이 될 때까지
n=25
k=3
count=0

while True:
  if n%k==0 :
    n /= k
    count +=1
    if(n==1): break
  else :
    n -= 1
    count +=1
    if(n==1): break

print(count)
