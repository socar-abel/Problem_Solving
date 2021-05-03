# p485 예제 B-1 소수구하기
import math
m, n = 3, 16
isPrime = [True]*(n+1)

for i in range(2,int(math.sqrt(n))+1):
  if isPrime[i] == True:
    x = 2
    while (i*x) <= n:
      isPrime[i*x] = False 
      x += 1

for i in range(2,len(isPrime)):
  if isPrime[i]:
    print(i,end= ' ')

print()


# B-2 암호 만들기 
from itertools import combinations
l, c = 4, 6
alphabet = ['a','t','c','i','s','w']
vowels = ('a','e','i','o','u')
for a in combinations(alphabet,l):
  mystr="".join(sorted(a))
  count = 0
  for s in mystr:
    if s in vowels:
      count += 1
  if count >= 1:
    print(mystr)

print()
