# 이코테 48제 - 그리디 - 모험가 길드

n = int(input())
array = list(map(int,input().split()))

array.sort() # O(log n)

i = len(array) - 1
count = 0

while True:
  if array[i] > i+1 : # array[3] = 4 인 경우 종료
    break
  else :
    temp = array[i]
    i = i - temp
    count += 1

print("The number of group :",count)
  
 
