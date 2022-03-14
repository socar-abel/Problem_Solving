from collections import deque
import sys
wheel = [[]]

for i in range(4):
    wheel.append(deque(list(map(int, sys.stdin.readline().strip()))))

K = int(sys.stdin.readline())
for _ in range(K):
    number, direction = map(int, sys.stdin.readline().split())
    # (톱니 번호, 방향)
    rotate_list = []

    # 1번 톱니가 돌아갈 때
    if number == 1:
        rotate_list.append((1, direction))
        if wheel[1][2] != wheel[2][6]:
            rotate_list.append((2, -direction))
            if wheel[2][2] != wheel[3][6]:
                rotate_list.append((3, direction))
                if wheel[3][2] != wheel[4][6]:
                    rotate_list.append((4, -direction))

    # 2번 톱니가 돌아갈 때
    elif number == 2:
        rotate_list.append((2, direction))
        if wheel[2][6] != wheel[1][2]:
            rotate_list.append((1, -direction))
        if wheel[2][2] != wheel[3][6]:
            rotate_list.append((3, -direction))
            if wheel[3][2] != wheel[4][6]:
                rotate_list.append((4, direction))

    # 3번 톱니가 돌아갈 때
    elif number == 3:
        rotate_list.append((3, direction))
        if wheel[2][2] != wheel[3][6]:
            rotate_list.append((2, -direction))
            if wheel[1][2] != wheel[2][6]:
                rotate_list.append((1, direction))
        if wheel[4][6] != wheel[3][2]:
            rotate_list.append((4, -direction))

    # 4번 톱니가 돌아갈 때
    elif number == 4:
        rotate_list.append((4, direction))
        if wheel[4][6] != wheel[3][2]:
            rotate_list.append((3, -direction))
            if wheel[3][6] != wheel[2][2]:
                rotate_list.append((2, direction))
                if wheel[2][6] != wheel[1][2]:
                    rotate_list.append((1, -direction))

    for n, d in rotate_list:
        wheel[n].rotate(d)

answer = 0
for x in range(1, 5):
    answer += wheel[x][0] * (2 ** (x-1))

print(answer)
