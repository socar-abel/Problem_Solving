'''
2021.02.09
부록 A - 4 : 함수, 5: 입출력 공부
'''

# 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우. 함수 안에서 global 키워드를 이용하면 된다. global 키워드로 변수를 지정하면, 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.
a=0
def func():
  global a
  a+=1

for i in range(10):
  func()
print(a)

# 람다 표현식 (Lambda Expression)

def add(a,b):
  return a+b

print(add(3,7))

print((lambda a,b: a+b)(3,7))

# 입출력
# ! 반드시 외워야 할 코드. 여러 개의 데이터를 입력받을 때 데이터가 공백으로 구분되는 경우.

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int,input().split()))

data.sort(reverse=True)
print(data)

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int,input().split())
print(n,m,k)

# 입력의 개수가 매우 많은 경우는 sys.stdin.readline() 함수를 이용하는게 시간적으로 이득이다.

import sys
data=sys.stdin.readline().rstrip()
print(data)

# 변수를 문자열로 바꾸어 출력하는 소스코드 예시
answer =7
print("정답은 "+str(answer)+"입니다.")

# 각 변수를 콤마로 구분하여 출력하는 소스코드 예시. 이 경우 공백이 삽입된다.
answer = 8
print("정답은",str(answer),"입니다.")

# f-string문법. 문자열 앞에 접두사 'f'를 붙임으로써 사용할 수 있다.
answer = 9
print(f"정답은 {answer}입니다.")
