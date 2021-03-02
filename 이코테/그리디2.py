'''
# 예제 3-1 거스름돈 (나의 코드)
n = 1260
count = 0

if n//500 >=1 :
  count += n//500
  n = n%500
  
if n//100 >=1 :
  count += n//100
  n = n%100
 
if n//50 :
  count += n//50
  n = n%50 

if n//10 :
  count += n//10
  n = n%10  

print(count)

# 예제 3-1 (책의 코드)
n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
  count += n//coin
  n = n%coin

print(count)


# 2 큰 수의 법칙 (나의 코드)
n,m,k = map(int, input().split()) 
array = list(map(int, input().split()))

array.sort(reverse=True)
first = array[0]
second = array[1] 

result = (first*k + second) * ( m // (k+1) ) + first * ( m % (k+1) )

print(result)

# 2 큰 수의 법칙 (책의 코드)) while문 도중에 탈출 조건을 입력하였다.
n, m, k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()  
first = data[n-1] # 뒤에서 첫번째
second = data[n-2] # 뒤에서 두번째 

result = 0

while True:
  for i in range(k):
    if m==0:
      break  
    result += first 
    m -= 1 
  if m == 0:
    break  
  result += second 
  m-=1 

print(result) 


# 3 숫자 카드 게임 
n, m = map(int, input().split())
graph = []

for _ in range(n):
  data = list(map(int,input().split()))
  graph.append(data)

mins = []

for i in range(n):
  now = min(graph[i]) 
  mins.append(now)

print('Result :',max(mins))


# 3-3 min()  함수를 이용하는 답안 예시 
n, m = map(int,input().split())

result = 0

for i in range(n):
  data = list(map(int,input().split()))
  min_value = min(data)
  result = max(result,min_value)

print(result)

# 3-4 2중 반복문 구조를 이용하는 답안 예시. 별로인 것 같다.
n,m = map(int,input().split())
result = 0 
for i in range(n):
  data = list(map(int,input().split()))
  min_value = 10001
  for a in data:
    min_value = min(min_value,a)
  result = max(result,min_value)

print(result) 

# 4. 1이 될 때까지 
n, k  = map(int,input().split())
count = 0 

while True:
  if n % k == 0 :
    n = n//k
    count+=1 
  else : 
    n-=1
    count+=1 
  if n==1:
    break  

print(count)

# 3-5 단순하게 푸는 답안 예시 
n, k = map(int, input().split())
result = 0 

# n이 k 이상이라면 k로 계속 나누기 
while n>=k:
  while n%k != 0:
    n-=1
    result+=1
  n//=k  
  result +=1 
while n<1:
  n==1
  result+=1
print(result) 
'''
# 3-6 답안 예시 
n, k = map(int, input().split())
result = 0 

while True:
  target = (n//k)*k
  result +=(n-target)
  n=target 
  if n<k:
    break  

  result+=1
  n//=k  
result+=(n-1)
print(result)
