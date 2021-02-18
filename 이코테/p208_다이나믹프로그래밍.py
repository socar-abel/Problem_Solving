'''
# 8-1 피보나치 함수 소스코드
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 8-2 피보나치 함수 소스코드 (메모이제시연, 캐싱 기법 사용)
d = [0]*100

def fibo(x):
  if x==1 or x==2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = fibo(x-1) + fibo(x-2)

  return d[x]

print(fibo(99))

# 8-3 호출되는 함수 확인
d = [0]*100

def pibo(x):
  print('f('+str(x)+')',end=' ')
  if x==1 or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  d[x] = pibo(x-1) + pibo(x-2)
  return d[x]
pibo(6)
print()


# 8-4 피보나치 수열 소스코드 (바텀업)
d = [0]*100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
  d[i] = d[i-1] + d[i-2]
print(d[n])


# 2. 1로 만들기

x = int(input())
d = [0]*30001

for i in range(2,x+1):
  d[i] = d[i-1] + 1
  if i%2 == 0:
    d[i] = min(d[i],d[i//2]+1)
  if i&3 == 0:
    d[i] = min(d[i],d[i//3]+1)
  if i%5 == 0:
    d[i] = min(d[i],d[i//5]+1)

print(d[x])


# 3. 개미 전사
# 8-6 답안예시
n = int(input())
array = list(map(int,input().split()))

d = [0]*100

d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
  d[i] = max(d[i-1],d[i-2]+array[i])

print(d[n-1])


# 4 바닥 공사
n = int(input())

d = [0]*1001
d[1]=1
d[2]=3
for i in range(3,n+1):
  d[i]=(d[i-1]+d[i-2]*2)%796796

print(d[n])


'''

# 5. 효율적인 화폐 구성
# 8-8 답안 예시
n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input()))

d = [10001] * (m+1)

d[0]=0
for i in range(n):
  for j in range(array[i], m+1):
    if d[j-array[i]] != 10001:
      d[j] = min(d[j],d[j-array[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])

