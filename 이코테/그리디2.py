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
'''

