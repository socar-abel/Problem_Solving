# Python Tip

1. List comprehension
2. 리스트 복사   
3. 슬라이싱 활용   
4. 간편한 이진탐색 bisect   
5. replace 함수를 활용한, 다조건 문자열 파싱   
6. lambda + sorted   


## 1. List comprehension
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
