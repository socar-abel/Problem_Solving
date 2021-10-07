import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    if s == '[]':
        num = deque([])
    else:
        num = s[1:-1].split(',')
        num = deque(num)

    error = False
    reverse = 0

    for x in p:
        if x == 'R':
            reverse = (reverse+1) % 2
        elif x == 'D':
            if not num:
                error = True
                break
            else:
                if reverse == 0:
                    num.popleft()
                elif reverse == 1:
                    num.pop()

    if error:
        print('error')
    else:
        if reverse == 1:
            print('[', end='')
            num.reverse()
            for x in range(len(num)):
                if x == len(num)-1:
                    print(num[x], end='')
                else: print(num[x], end=',')
            print(']')

        else:
            print('[', end='')
            for x in range(len(num)):
                if x == len(num) - 1:
                    print(num[x], end='')
                else:
                    print(num[x], end=',')
            print(']')
