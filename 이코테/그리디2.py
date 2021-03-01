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
'''
# 예제 3-1 (책의 코드)
n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
  count += n//coin
  n = n%coin

print(count)
