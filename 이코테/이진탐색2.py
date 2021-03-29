'''
# 재귀함수로 구현한 이진 탐색 코드
# binary search with recursion
def binary_search(array, target, start, end):
  if start > end :
    return None
  mid = (start + end)//2
  if target < array[mid]:
    binary_search(array, target, start, mid-1)
  elif target > array[mid]:
    binary_search(array, target, mid+1, end)
  else :
    return mid

n, target = list(map(int,input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
  print("There is no target")
else :
  print(result)


# 반복문으로 구현한 이진 탐색 코드
# binary search with while loop
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end)//2 
    if target == array[mid]:
      return mid 
    elif target < array[mid]:
      end = mid-1
    else :
      start = mid+1 
  return None

n, target = list(map(int,input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
  print("There is no target")
else :
  print(result)


# 부품 찾기
n = int(input())
arrayN = list(map(int,input().split()))

m = int(input())
arrayM = list(map(int,input().split()))

count = 0
for i in arrayN:
  if i in arrayM:
    count+=1 

if count == m:
  print("yes")
else :
  print("no")

'''

# 떡볶이 떡 만들기 (이거 진짜 도대체 왜 None이라고 나옴 ?)
# 와 이해됨 반드시 return binary_search(..)로 호출해야 함
n, m = map(int,input().split())
array = list(map(int,input().split()))
maxlen = max(array)

def binary_search(array, target, start, end):
  if start > end:
    return 999
  total = 0
  mid = (start+end)//2 
  print('mid :',mid)
  for a in array :
    if mid < a:
      total += a-mid
    else :
      pass
  
  if target == total:
    return mid 
  elif target < total:
    return binary_search(array,target,mid+1,end)
  else :
    return binary_search(array,target,start,mid-1)

result = binary_search(array, m ,0, maxlen)

print(result)
