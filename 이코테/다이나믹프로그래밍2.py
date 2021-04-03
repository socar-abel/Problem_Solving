'''
# sol1) Fibonacci Function with recursion 
def fibo(x):
  if x==1 or x==2:
    return 1
  else: return fibo(x-1) + fibo(x-2)

print(fibo(4))

# sol2) But if x is a large integer, sol1 will be not efficient.
# In that case it is better that using memoization. (Top-Down)
d = [0]*100 

def fibo_TopDown(x):
  if x==1 or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  else :
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo_TopDown(99))

# sol3) Bottom-up
d = [0]*100
d[1]=1
d[2]=1

def fibo_BottomUp(x):
  for i in range(3,x+1):
    d[i]=d[i-1]+d[i-2]
  return d[x]
  
print(fibo_BottomUp(99))
'''

# 1로 만들기 
x = int(input())

def myfunc(n):
  if n==1 : return 0

  if n==2 or n==3 or n==5:
    return 1
  
  candidate = []
  candidate.append(myfunc(n-1))
  if n%5==0:
    candidate.append(myfunc(n/5))
  elif n%3==0:
    candidate.append(myfunc(n/3))
  elif n%2==0:
    candidate.append(myfunc(n/2))
  
  return min(candidate)+1

print(myfunc(x))

# + 메모이제이션
x = int(input())
d = [0]*30001

for i in range(2,x+1):
  if i==2 or i==3 or i==5:
    d[i]=1
  candidate = []
  candidate.append(d[i-1])
  if i%5==0:
    candidate.append(d[i//5])
  if i%3==0:
    candidate.append(d[i//3])
  if i%2==0:
    candidate.append(d[i//2])
  d[i] = min(candidate) + 1

print(d[x])
