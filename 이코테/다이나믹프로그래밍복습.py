'''
# 8-1 피보나치 함수 (재귀함수 이용)
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1)+fibo(x-2)

print(fibo(4))

# 8=2 피보나치 함수 (재귀함수, 메모이제이션 이용)
d = [0]*100

d[1]=1
d[2]=1

def fibo(x):
  if not d[x]==0:
    return d[x]
  d[x]=fibo(x-1)+fibo(x-2)
  return d[x]

print(fibo(99))  

# 8-4 피보나치 함수 (바텀업, 반복문 이용)

d = [0]*100
d[1]=1
d[2]=1
x=99

for i in range(3,x+1):
  d[i]=d[i-1]+d[i-2]

print(d[x])

# 1로 만들기
d = [0]*30001
n = int(input())

for i in range(2,n+1):
  d[i]=d[i-1]+1
  if i%5==0:
    d[i]=min(d[i],d[i//5]+1)
  if i%3==0:
    d[i]=min(d[i],d[i//3]+1)  
  if i%2==0:
    d[i]=min(d[i],d[i//2]+1)

print(d[n])  

# 개미 전사
n = int(input())
d=[0]*n
array = list(map(int,input().split()))

for i in range(n):
  if i==0:
    d[i]=array[i]
  if i==1:
    d[i]=max(array[i-1],array[i])
  d[i] = max(d[i-1],d[i-2]+array[i])

print(d[n-1])


# 4 바닥 공사
n = int(input())
d=[0]*1001
d[1]=1
d[2]=3
for i in range(3,n+1):
  d[i]=(d[i-1]+d[i-2]*2)%796796
print(d[n])

'''

# 5 효율적인 화폐 구성
n, m = map(int, input().split())

array=[]
for i in range(n):
  array.append(int(input()))

d = [10001]*(m+1)
d[0]=0

for i in range(n):
  for j in range(array[i],m+1):
    if d[j-array[i]]!=10001:
      d[j] = min(d[j],d[j-array[i]]+1)
if d[m]==10001:
  print(-1)
else:
  print(d[m])
