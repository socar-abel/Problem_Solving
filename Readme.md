# Python Tip ## Kim Sang Woo

1. 리스트 컴프리헨션
2. 리스트 복사   
3. 슬라이싱 활용   
4. 간편한 이진탐색 bisect   
5. replace 함수를 활용한, 다조건 문자열 파싱   
6. lambda + sorted   
7. 리스트에서의 중복 제거
8. 문자열과 리스트
9. 문자열 숫자/알파벳 판별 - isdigit(), isalpha()
10. 파이썬 for문의 index
11. pass와 continue의 차이 
12. 빈 리스트일때의 return ... or 사용법  
13. upper와 lower   
14. in 활용법
15. return True or False 간략화
16. 문자열 곱셈 활용
## 1. 리스트 컴프리헨션 (List comprehension)
<pre>
<code>
10 이하의 짝수를 담는 리스트 컴프리헨션  

list = [x for x in range(1,10+1) if x % 2 == 0]
--> list = [2,4,6,7,10]
</code>
</pre>
 
   
<pre>
<code>
0~4 의 수에서 짝수면 숫자를, 홀수면 odd를 담는 방법   

list = [x if x % 2 == 0 else 'odd' for x in range(5)]
--> list = [0,odd,2,odd,4]
</code>
</pre>



## 2. 리스트 복사

파이썬 리스트에서는 deep copy와 shallow copy가 일어난다.
<pre>
<code>
listA = [1,2,3]
listB = listA
listB[0] = 100
</code>
</pre>
위와 같이 코드를 작성한 경우      
<code>listA = [100,2,3]</code> 으로 함께 변경된다.
   
따라서 제대로 된 복사(deep copy)를 하고 싶은 경우   
<code>listB = listA[:] </code> 
와 같이 코드를 작성해야 한다.   
   
    
   
## 3. 슬라이싱 활용
<code>listA = [1,2,3,4,5]</code>를 역순으로 사용하고 싶다면   
<code>listB = listA[::-1]</code>와 같이 활용하면 된다.
   
<code>1,3,5</code>와 같이 2칸씩 띄고 싶다면   
<code>listB = listB[::2]</code>와 같이 활용하면 된다.

## 4. 간편한 이진탐색 bisect
Python에서는 bisect를 지원한다.   
<pre>
<code>
from bisect import bisect_left, bisect_right
array = [10,10,10,20,30,30,40,40,40,40,40,60,70,80,80,90]

cutLine = 30
index1 = bisect_left(array,cutLine)
index2 = bisect_right(array,cutLine)
print(index1,index2)
</code>
</pre>

-> 출력 : <code>4 6</code>

## 5. replace 함수를 활용한, 다조건 문자열 파싱
카카오 - 순위 검색 문제   
'and'도 파싱해야 하고, ' '도 파싱해야 하는 상황   
<code>replace(' and ', ' ').split(' ')</code>   
-> ' and '를 ' '로 대체시킨 후, ' '를 기준으로 쪼갠다.

## 6. lambda + sorted 
   
<pre>
<code>
c = sorted(a, key = lambda x : x[0])
</code>
</pre>

리스트 a에서 0번째 값을 key로 sorting 하는 방법.

## 7. 리스트에서의 중복제거
<pre>
<code>
listA = [2,2,3,3,3,4,5,6,6,...]  # 정렬된 리스트
listA = list(set(listA)) # 중복제거
listA.sort()  # 재정렬
</code>
</pre>
set을 이용해서 중복제거를 할 수 있지만, set을 사용하면 순서가 뒤섞이기 때문에 다시 sort()해줘야 한다.

## 8. 문자열과 리스트
문자열에서는 마치 리스트처럼 한 글자마다 번호를 새긴다.
<pre>
<code>
x = 'banana'

--> x[0] = 'b'
--> x[2:4] = 'na'
</code>
</pre>

하지만 문자열에 있는 글자를 리스트처럼 접근해서 변경할 수는 없다.
<pre>
<code>
x[0] = 'n' 
--> 불가능 !

꼭 바꾸고 싶다면 다음과 같이 할 수 있다.
방법 1)
x = 'n' + x[1:]
--> x = 'nanana'

방법 2)
x = list(x)
x[0] = n
x = "".join(x)

</code>
</pre>

## 9. 문자열 숫자/알파벳 판별 - isdigit(), isalpha()
<pre>
<code>
ex1 = '1'
ex2 = 'A'
print(ex1.isdigit(), ex2.isalpha())
</code>
</pre>

결과 : <code>True True</code>

## 10. 파이썬 for문의 index
C++의 for문은   
<code>for(int i=0; i<10; i++)</code>   
처럼 쓰고 특정 조건일때 i의 값을 변경하면 조건문의 횟수를 조절할 수 있다.   
   
하지만 Python에서는 for문 안에서 i 값을 변경하면 그 반복문 내에서는 반영되지만, 다음 반복시에는 원래의 i값(다음값)으로 돌아간다.
다음 예시는 1,2,3,4,5 를 가진 리스트에서, 3을 만날경우 건너뛰고 싶은 상황이다.
<pre>
<code>
# 잘못된 예시
arr = [1,2,3,4,5]

for a in arr :
  if a == 3:
    a += 1
  print(a,end = ' ')
print()  # 결과 --> 1 2 4 4 5

# 해결법
a = 0
while a < len(arr):
  if arr[a] == 3:
    a += 1
  print(arr[a],end = ' ')
  a += 1
print()  # 결과 --> 1 2 4 5
</code>
</pre>
   
## 11. pass와 continue의 차이
pass : 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행한다.   
continue : 바로 다음 순번의 loop를 수행한다.  

## 12. 빈 리스트일때의 return ... or 사용법
answer = [...] 라는 리스트가 있을 때,
<pre>
<code>
...
return answer or [-1]
</code>
</pre>
다음과 같이 코드를 작성하면 answer가 비어있는 리스트일 경우 [-1]를 리턴한다.
   
## 13. upper와 lower
<pre>
<code>
str = "Kim Sang Woo"
print(str.upper())
print(str.lower())
</code>
</pre>
결과 : 
<code> 
KIM SANG WOO, 
kim sang woo
</code>   
참고로 isupper와 islower도 존재하고, 정렬하였을 때 대문자가 소문자보다 앞에 위치한다.

## 14. in 활용법
x 가 3,4,6,7 인 경우를 체크하고 싶을때, if와 elif를 반복할 필요없이
<pre>
<code>
if x in [3,4,6,7]:
</code>
</pre>
와 같이 코드를 작성하면 깔끔하다.

## 15. return True or False 간략화
예를들어, x가 짝수면 True, 홀수면 False를 리턴하는 함수를 생각해보자.
<pre>
<code>
# 내가 짜던 코드
def func(x):
 return True if x % 2 == 0 else False

# 간략화
def func2(x):
 return x % 2 == 0
</code>
</pre>   
if문을 사용하지 않아도 True와 False를 판단하여 리턴한다.

## 16. 문자열 곱셈 활용
숫자가 나열된 문자열에서 마지막 4자리를 제외한 모든 숫자를 *로 변경하고 싶을 경우.
<pre>
<code>
# 내가 전에 짰던 코드

def solution(phone_number):
    plist = list(phone_number)
    for i in range(len(plist)-4):
        plist[i] = "*"
    
    return "".join(plist)

# 문자열 곱셈을 이용하면 for문을 사용할 필요가 없어진다.

def solution(phone_number):
    
    return "*" * ( len(phone_number)-4 ) + phone_number[-4:]
</code>
</pre>
