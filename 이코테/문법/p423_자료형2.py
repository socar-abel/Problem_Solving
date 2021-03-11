'''
2021.02.08
부록 A 

'''

# 특정 크기의 2차원 리스트를 초기화 할 때는 반드시 리스트 컴프리헨션을 이용해야 한다. 만약 다음과 같이 N x M 크기의 2차원 리스트를 초기화 한다면, 의도하지 않은 결과가 나올 수 있다.
# 실행 결과를 확인해보면 array[1][1]의 값을 5로 바꾸었을 뿐인데, 3개의 리스트에서 인덱스 1에 해당하는 원소들이 모두 5로 바뀐 것을 확인 할 수 있다.
# 이는 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문이다. 
n=3
m=4
array=[[0]*m]*n
print(array)

array[1][1]=5
print(array)

# 리스트 컴프리헨션을 이용한 초기화. 정상적으로 작동한다.
n=3
m=4
array=[[0]*m for _ in range(n)]
array[1][1]=4
print(array)

# 복습 : 1~20 의 수 중 홀수만 넣는 리스트
oddArray = [i for i in range(1,21) if i%2 == 1]
print(oddArray)

# 복습 : 1 부터 9 까지의 수의 제곱 값을 포함하는 리스트
squareArray = [i**2 for i in range(1,10)]
print(squareArray)

squareArray.reverse()
print(squareArray)

# 리스트 관련 메서드
a=[1,4,3]
print("기본 리스트: ",a)
a.append(2)
print("append(2) :",a)
a.sort()
print("sort() :",a)
a.sort(reverse = True)
print("sort(reverse=True) :",a)
a.reverse()
print("reverse() :",a)
a.insert(2,3)
print("insert(2,3) :",a)
print("a.count(3) :",a.count(3))
a.remove(1)
print("remove(1) :",a)

# a의 특정한 값의 원소를 모두 제거하기 위한 코드
# 너무 편한듯.. 
# result : i를 저장할 것이고, i는 a에 있는 원소들이다. i는 remove_set에 들어있으면 안된다.
a=[1,2,3,4,5,5,5]
remove_set=[3,5]

result = [i for i in a if i not in remove_set]

# 문자열 자료형
# 문자열 연산
a = "Hello"
b = "World"
print(a+" "+b)

a = "String\n"
print(a*3)

# 파이썬의 문자열은 내부적으로 리스트와 같이 처리된다
# 문자열은 여러 개의 문자가 합쳐진 리스트라고 볼 수 있다. 따라서 문자열 데이터에 대해서도 마찬가지로 인덱싱과 슬라이싱을 이용할 수 있다.
a="ABCDEF"
print(a[2:4])

# 튜플 자료형
# 파이썬의 튜플 자료형은 리스트와 거의 비슷한데 다음과 같은 차이가 있다.
# 1. 튜플은 한 번 선언된 값을 변경할 수 없다.
# 2. 리스트는 대괄호[]를 이용하지만, 튜플은 소괄호()를 이용한다.
# 튜플 자료형은 그래프 알고리즘을 구현할 때 자주 사용된다. 
# 알고리즘을 구현하는 과정에서 일부러 튜플을 이용하게 되면 혹여나 자신이 알고리즘을 잘못 작성함으로써 변경하면 안 되는 값이 변경되고 있지는 않은지 체크할 수 있다.

a=(1,2,3,4)
print(a)
# a[2]=7 불가능.

# 사전 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

# data에 특정한 원소가 있는지 검사하는 문법. 리스트나 튜플에서도 사용 가능하다.
if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 파이썬에서 리스트, 문자열, 튜플 등 순차적인 정보를 담는 자료형을 iterable 자료형 이라고 한다. in 문법은 위와같은 iterable 자료형에 모두 사용이 가능하다.

# 사전 자료형 관련 함수
# 키와 값을 별도로 뽑아내기 위한 함수가 있다. 키 데이터만 뽑아서 리스트로 이용할 때는 keys() 함수를 이용하며, 값 데이터만 뽑아서 리스트로 이용할 때는 values() 함수를 이용한다.

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
  print(data[key])

# 집합 자료형
# 파이썬 에서는 집합(set)을 처리하기 위한 집합 자료형을 제공하고 있다.
# 집합은 기본적으로 리스트 혹은 문자열을 이용해서 만들 수 있는데, 집합은 다음과 같은 특징이 있다.
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다.
# 기존에 다루었던 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있었다. 반면에 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다는 특징이 있다.
# 집합 자료형은 특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 매우 효과적이다. 초기화 하는 방법은 set() 함수를 이용하거나, { , , } 로 표기한다.

data= set([1,1,2,3,4,4,5])
print(data)

data={1,1,2,3,4,4,5}
print(data)

# 집합 자료형의 연산 
# 합집합 | , 교집합 & , 차집합 -
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b)
print(a&b)
print(a-b)

# 집합 자료형 관련 함수
# 하나의 집합 데이터에 값을 추가 할 때는 add() 함수를 이용한다.
# update() 함수는 여러 개의 값을 한꺼번에 추가하고자 할 때 사용한다.
# 특정한 값을 제거할 때는 remove() 함수를 이용 할 수 있다.squareArray
data = set([1,2,3])
print(data)

data.add(4)
print(data)

data.update([3,4,5,6])
print(data)

data.remove(3)
print(data)

# 파이썬 참 신기하고 재밌다.
