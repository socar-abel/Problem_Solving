# 투 포인터즘을 이용한 문제 풀이

# 1. 특정한 합을 가지는 부분 연속 수열 찾기
n = 5
m = 5 # 찾고자 하는 부분 합
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복 
for start in range(n):
  # end를 가능한 만큼 이동시키기
  while interval_sum < m and end < n:
    interval_sum += data[end]
    end += 1

  if interval_sum == m:
      count += 1
  interval_sum -= data[start]

print(count)

# 2. 정렬되어 있는 두 리스트의 합집합 구하기
n, m = 3, 4
a = [1,3,5]
b = [2,4,6,8]

result = [0] * (n+m)
i = 0 
j = 0
k = 0

while i < n or j < m:
  # 리스트 B의 모든 원소가 처리 되었거나, 
  # 리스트 A의 원소가 더 작을 때
  if j >= m or (i < n and a[i] <= b[j]):
    result[k] = a[i]
    i += 1
  # 리스트 A의 모든 원소가 처리 되었거나, 
  # 리트스 B의 원소가 더 작을 때
  else :
    result[k] = b[j]
    j += 1
  k += 1

for i in result:
  print(i, end = ' ')
