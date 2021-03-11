'''
2021.02.05

1. 이걸 풀면서 느낀점 : 그럼 컴퓨터 성능에 따라 time limit error가 뜰 수도 있고 안뜰수도 있다는 건가 ? ?

2. 선택 정렬 알고리즘은 O(N^2) time 이 소요된다.

3. repl.it IDE가 편리함을 느낌. 그런데 Run을 돌리면 main.py가 돌아가는데 계속 불편하게 shell에서 python 파일명.py를 실행해야 하는 건가?
빌드에서 제외하는 방법이 있을 것 같은데 못 찾겠음.

4. how to ~ in repl.it 
이런 식으로 구글링하면 정보 검색 가능.
저장은 자동으로 지원되며, main.py만 작동되는게 맞다고 함.
main.py에 다른 python파일을 가져와서 실행하는 것을 권장한다고 함.

'''

from random import randint
import time

#배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))  # 1부터 100 사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i+1,len(array)):
    if array[min_index]>array[j]:
      min_index=j
  array[i], array[min_index] = array[min_index], array[i] # 스와프

end_time = time.time()
print("선택 정렬 성능 측정:", end_time-start_time) # 수행시간 출력

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time() # 측정 종료
print("기본 정렬 라이브러리 성능 측정:",end_time-start_time)
