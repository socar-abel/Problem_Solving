
입력값은 Dictionary형태로 넣어주면, 결과값 또한 Dictionary이다.

# collections.Counter 예제 (2)
# dictionary를 입력값으로 함

import collections

print(collections.Counter({'가': 3, '나': 2, '다': 4}))

'''
결과
Counter({'다': 4, '가': 3, '나': 2})
'''
3) 값 = 개수 형태
collections.Counter()에는 값=개수형태로 입력이 가능하다.
예를들어, collections.Counter(a=2, b=3, c=2)는 ['a', 'a', 'b', 'b', 'b', 'c', 'c']와 같다.
아래의 예제(3)의 출력값을 통해 확인할 수 있다.

# collections.Counter 예제 (3)
# '값=개수' 입력값으로 함

import collections

c = collections.Counter(a=2, b=3, c=2)
print(collections.Counter(c))
print(sorted(c.elements()))

'''
결과
Counter({'b': 3, 'c': 2, 'a': 2})
['a', 'a', 'b', 'b', 'b', 'c', 'c']
'''
4) 문자열(String)
예제(4)에서 볼 수 있듯이, 문자열을 입력했을 경우 {문자 : 개수}의 딕셔너리 형태로 반환해 준다.

# collections.Counter 예제 (4)
# '문자열'을 입력값으로 함

import collections

container = collections.Counter()
container.update("aabcdeffgg")
print(container)

'''
결과
Counter({'f': 2, 'g': 2, 'a': 2, 'e': 1, 'b': 1, 'c': 1, 'd': 1})
'''

for k,v in container.items():
    print(k,':',v)

'''
결과
f : 2
e : 1
b : 1
g : 2
c : 1
a : 2
d : 1
'''


출처: https://excelsior-cjh.tistory.com/94 [EXCELSIOR]
