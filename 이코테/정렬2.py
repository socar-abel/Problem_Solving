 # 6-1 선택 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4]

for i in range(len(array)):
  min_index = i
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index=j
      
  array[min_index], array[i] = array[i], array[min_index]

print(array)
