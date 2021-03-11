# 부록 A-6. 주요 라이브러리의 문법과 유의점

## 내장 함수

# sum() 함수는 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환한다. 리스트의 모든 값을 더하는 예시를 확인해보자.
result = sum([1,2,3,4,5])
print(result)

# min() 함수는 파라미터가 2개 이상 들어있을 때 가장 작은 값을 반환한다. 예를 들어 특정한 4개의 정수 중에서 가장 작은 수를 출력하는 예시를 확인해보자.

a = (7,3,5,2)
aMin = min(a)
aMax = max(a)
print(a)
print("min :",aMin,"max : ",aMax)

s = "(3+5)*7"
print(s)
print("result :",eval(s))

# 파이썬에서는 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행할 수 있다. 정렬 기준은 key 속성을 이용해 명시 할 수 있다.
# 튜플의 두 번째 원소를 기준으로 내림차순으로 정렬하기
a = [('홍길동',35),('이순신',75),('아무개',50)]
print(a)
a.sort(key=lambda x:x[1],reverse=True)
print("result :",a)



## itertools
# itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다. permutations, combinations, product, combinations_with_replacement 를 포함한다.
# 각각 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.

# permutations. 순열
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3))
print("Permutations :",result)
print()

# combinations. 조합
from itertools import combinations
data = ['A','B','C']
result = list(combinations(data,2))
print("Combinations :",result)
print()

# product. 중복 순열. product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다. 다만 원소를 중복하여 뽑는다.
from itertools import product
data = ['A','B','C']
result = list(product(data,repeat=2))
print("Product :",result)
print()

# 중복 조합. combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다. 다만 원소를 중복해서 뽑는다.
from itertools import combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data,2))
print("Combinations_with_replacement :",result)
print()


## heapq
# 힙 기능을 위한 라이브러리. 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.

# Heap Sort를 heapq로 구현하는 예제
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h,value)
    print(h)
  print("h :",h)
  print("len(h) :",len(h)) 
  #힙에 삽입된 원소를 차례대로 꺼내어 담기
  for i in range(len(h)): # 반드시 range(len(h))를 이용해 함. 그냥 h는 안됨.
    i = heapq.heappop(h)
    result.append(i)
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 최대 힙 구현 방법 (내림차순)

def maxHeapsort(iterable):
  h=[]
  result = []

  for value in iterable:
    heapq.heappush(h,-value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result
result = maxHeapsort([1,3,5,7,9,2,4,6,8,0])
print("Max Heap Sort : ",result)


## bisect
# 파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다. bisect 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.

from bisect import bisect_left, bisect_right

a=[1,2,4,4,8]
x=4
print("List a :",a)
print("bisect_left(a,x) :",bisect_left(a,x))
print("bisect_right(a,x) :",bisect_right(a,x))

# 또한 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 때 효과적으로 사용될 수 있다.

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a,right_value)
  left_index = bisect_left(a,left_value)
  return right_index-left_index

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))


## collections 
# 파이썬의 collection 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리다. collections 라이브러리의 기능 중에서 코딩 테스트에 유용하게 사용되는 클래스는 deque (덱) 와 Counter이다.
# deque : 양끝의 어느 쪽에서든 데이터의 출입이 가능한 데이터 행렬

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print("deque :",data)
print("list :",list(data))

from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])
a = ['red','blue','red','green','blue','blue']

print("counter['blue'] :",counter['blue'])
print("counter['green'] :",counter['green'])
print("a.count('blue') :",a.count('blue'))

print(dict(counter))

## math
# math 라이브러리는 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수GCD 등을 계산해주는 기능을 포함한다.

import math
print("5! :",math.factorial(5))
print("7의 제곱근 :",math.sqrt(7))
print("21과 14의 최대공약수 :",math.gcd(21,14))

print("pi :",math.pi)
print("자연상수 e :",math.e)
