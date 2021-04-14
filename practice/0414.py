
'''
# 파이썬의 장점을 살린 퀵 소트
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array) <= 1 :
    return array 
  
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
'''
# 교재의 퀵 소트를 파이썬으로 구현 (while문으로 partition 수행)
from collections import deque
array = deque([5,7,9,0,3,1,6,2,4,8])


def quick_sort2(array):
  L = deque([])
  E = deque([])
  G = deque([]) 

  if len(array) <= 1:
    return array
  
  pivot = array.popleft()
  E.append(pivot)
  
  while array:
    y = array.popleft()
    if y < pivot:
      L.append(y)
    elif y == pivot:
      E.append(y)
    else :
      G.append(y)
  return quick_sort2(L) + E + quick_sort2(G)

print(quick_sort2(array))
