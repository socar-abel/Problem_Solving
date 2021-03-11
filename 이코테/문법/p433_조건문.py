# 부록 A - 조건문 공부
# if, elif, else 
score = 85
grade = 'A'
if score >= 90:
  grade = 'A'
elif score >= 80:
  grade = 'B'
elif score >= 70:
  grade = 'C'
else :
  grade = 'F'
print("학점 :",grade)

# 조건부 표현식
score = 85
result =  "Success" if score>=80 else "Fail"

# 조건부 표현식은 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용할 수 있다.
# 예를 들어 리스트에서 특정한 원소의 값만을 없앤다고 해보자. 원래ㅐ 일반적인 형태의 조건문을 이용하면 다음과 같이 작성해야 한다.
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = []
for i in a:
  if i not in remove_set:
    result.append(i)
print(result)

# 위의 코드는 다음과 같이 간단하게 작성할 수 있다.
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
print(result)

# 파이썬 조건문 내에서의 부등식
# 다른 언어와 달리 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다. 예를 들어 "x>0 and x<20"과 "0<x<20"은 같은 결과를 반환한다.
