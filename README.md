# Python Tip

## 1. 리스트 복사

파이썬 리스트에서는 깊은 복사와 얕은 복사가 일어난다.
<pre>
<code>
listA = [1,2,3]
listB = listA
listB[0] = 100
</code>
</pre>
위와 같이 코드를 작성한 경우      
<code>listA = [100,2,3]</code> 으로 함께 변경된다.
   
따라서 제대로 된 복사를 하고 싶은 경우   
<code>listB = listA[:] </code> 
와 같이 코드를 작성해야 한다.   
   
    
   
## 2. 슬라이싱 활용
<code>listA = [1,2,3,4,5]</code>를 역순으로 사용하고 싶다면   
<code>listB = listA[::-1]</code>와 같이 활용하면 된다.
   
<code>1,3,5</code>와 같이 2칸씩 띄고 싶다면   
<code>listB = listB[::2]</code>와 같이 활용하면 된다.

## 3. 간편한 이진탐색
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
