import sys
from collections import deque
N, K = map(int, input().split())
s = list(map(int, sys.stdin.readline().split()))
belt = deque([])
countingZero = 0

for x in s:
    # 칸에 로봇이 없음, 내구도
    belt.append([False, x])

step = 0
while True:
    step += 1
    # 1.벨트 회전
    belt.rotate(1)
    # - 내리는 위치에 도달하면 내림
    if belt[N-1][0]:
        belt[N-1][0] = False

    # 2.이동할 수 있다면 이동
    for i in reversed(range(2*N)):
        # 로봇이 없는 벨트는 이동 고려할 필요없음
        if not belt[i][0]: continue
        next = i+1
        if i == 2*N-1:
            next = 0
        # 로봇이 없고, 내구도가 1 이상이라면 이동.
        if not belt[next][0] and belt[next][1] >= 1:
            belt[next][0] = True
            belt[next][1] -= 1
            belt[i][0] = False
            if belt[next][1] == 0: countingZero += 1
            # 내리는 곳이면 내림.
            if next == N-1:
                belt[next][0] = False

    # 3. 올리기
    if not belt[0][1] == 0:
        belt[0][0] = True
        belt[0][1] -= 1
        if belt[0][1] == 0: countingZero += 1

    # 4. 과정 종료
    if countingZero >= K: break

print(step)

