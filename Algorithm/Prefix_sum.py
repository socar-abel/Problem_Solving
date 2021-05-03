# 접두사 합(Prefix Sum)을 이용한다.
n = 5
data = [10,20,30,40,50]

# 접두사 합 (Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)

# data[2]~data[4] 구간합 구하기 
left = 2
right = 4
print(prefix_sum[right]-prefix_sum[left-1])
