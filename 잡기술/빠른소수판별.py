import math

# 소수 판별 함수 O(X) time 
def is_prime_number(x):
  for i in range(2,x):
    if x % i ==0:
      return False
  return True 

# 소수 판별 함수 O(X^(1/2)) time
def is_prime_number2(x):
  for i in range(2,int(math.sqrt(x)+1)) :
    if x % i == 0 :
      return False 
  return True

# 범위 내의 모든 소수 구하기
# 에라토스테네스의 체 O(N*log(logN)) time
n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
  if array[i] == True:  # 소수인 경우
    j = 2
    while (i*j) <= n:
      array[i*j] = False
      j += 1

for i in range(2,n+1):
  if array[i]:
    print(i,end = ' ')
print()
