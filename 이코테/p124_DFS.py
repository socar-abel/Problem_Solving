'''
2021.02.14
DFS/BFS

# 5-1 스택 예제
# 파이썬에서 스택을 이용할 때는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작한다.
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()

stack.append(1)
stack.append(4)
stack.pop() 

print(stack)
print(stack[::-1])

# 5-2 큐 예제
# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용한다. deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다. 

from collections import deque

# 큐 (Queue)구현을 위해 deque 라이브러리 사용 
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() 
queue.append(1)
queue.append(4)
queue.popleft() 

print(queue)
queue.reverse() 
print(queue) 
print(list(queue)) # list(queue)를 하면 리스트 자료형으로 반환된다.


# 5-4 재귀함수 종료 예제
def recursive_function(i):
  # 10번째 출력했을 때 종료되도록 종료 조건 명시
  if i==10:
    return
  print(i,"번째 재귀함수에서",i+1,"번째 재귀 함수를 호출합니다.")
  recursive_function(i+1)
  print(i,"번째 재귀함수를 종료합니다.")

recursive_function(1)
'''

# 5-5 2가지 방식으로 구현한 팩토리얼 예제
# 반복적으로 구현한 5!
result = 1
for i in range(1,6):
  result *= i 
print("5! =",result) 

# 재귀적으로 구현한 5!
def recursive(i):
  if i<=1 : return 1
  return i*recursive(i-1)

print("5! =",recursive(5))

