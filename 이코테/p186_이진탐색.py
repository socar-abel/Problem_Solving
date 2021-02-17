'''
# 7-1 순차 탐색 소스코드
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
  # 각 원소를 하나씩 확인하며
  for i in range(n):
    # 현재의 원소가 찾고자 하는 원소와 동일한 경우
    if array[i] == target:
      return i+1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")

input_data = input().split() 
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")

array = input().split()
# 순차 탐색 수행 결과 출력
print(sequential_search(n,target,array))


# 7-2 재귀 함수로 구현한 이진 탐색 코드
def binary_search(array, target, start, end):
  if start>end:
    return None
  mid = (start+end)//2

  if array[mid]==target:
    return mid
  elif array[mid]>target:
    return binary_search(array, target, start, mid-1)
  else :
    return binary_search(array, target, mid +1 , end)

n, target = list(map(int, input().split()))

array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
  print("원소가 존재하지 않습니다.")
else: print(result+1," 번째에 있습니다.")


# 7-3 반복문으로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
  while start<=end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid-1
    else:
      start = mid+1
  return None

n, target = list(map(int, input().split()))

array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
  print("원소가 존재하지 않습니다.")
else: print(result+1," 번째에 있습니다.")


# 2 부품 찾기. 나의 풀이가 더 간결하다.
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in range(m):
  if b[i] in a:
    print('yes',end=' ')
  else:
    print('no',end=' ')
print()


# 7-5. 답안예시. 2. 부품찾기 (이진탐색 이용)
def binary_search(array, target, start, end):
  while start<=end:
    mid = (start+end)//2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid-1
    else :
      start = mid+1
  return None

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

for i in b:
  result = binary_search(a,i,0,n-1)
  if result != None:
    print('yes', end=' ')
  else:
    print('no',end=' ')
print()

# 7-6 답안 예시. 2. 부품찾기 (계수 정렬 사용)
n = int(input())
array = [0]*1000001

# 리스트를 입력받음과 동시에 1로 초기화. 문법 기억하기.
for i in input().split():
  array[int(i)]=1

m = int(input())
x = list(map(int,input().split()))

for i in x:
  if array[i] == 1:
    print('yes', end = ' ')
  else:
    print('no',end=' ')

'''

# 3 떡볶이 떡 만들기
n, m = map(int, input().split())

a = list(map(int,input().split()))

a.sort() 

start = 0
end = max(a)

result = 0

while start<=end:
  mid = (start+end)//2
  s = 0
  for x in a:
    if mid < x:
      s += x-mid

  print('s :',s)

  if s < m:
    end = mid-1
  else:
    result = mid
    start = mid+1 
    

print('result :',result)


