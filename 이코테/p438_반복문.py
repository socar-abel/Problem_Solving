# 부록 A - 반복문 공부
# while을 이용하여 1부터 9까지의 수 중에서 홀수만 더하기
i=1
result=0

while i<=9:
  if i%2==1:
    result+=i
  i+=1
print(result)

# for문으로 같은 코드 작성하기
i=1
result=0

for i in range(1,10):
  if i%2==1:
    result+=i
print(result)

scores = [90,85,77,65,97]
black_list = [2,4]
for i in range(5):
  if i+1 in black_list:
    continue
  if scores[i]>=80:
    print(i+1,"번 학생은 합격입니다.")

# 2중 for문으로 구구단
for i in range(2,10):
  for j in range (1,10):
    print(i,"X",j,"=",i*j)
  print()

