# Python Tip

## 1. 문자열 복사

파이썬 리스트에서는 깊은 복사와 얕은 복사가 일어난다.   
<pre>
<code>
listA = [1,2,3]   
listB = listA   
listB[0] = 100 
</code>
</pre>
위와같은 경우      
listA = [100,2,3] 으로 함께 변경된다.
   
따라서 제대로 된 복사를 하고 싶은 경우   
listB = listA[:]   
와 같이 코드를 작성해야 한다.
