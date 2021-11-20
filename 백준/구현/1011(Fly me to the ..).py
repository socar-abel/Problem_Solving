import sys
T = int(sys.stdin.readline())


def program():
    x, y = map(int, sys.stdin.readline().split())

    left = 0
    right = 0

    gap = y-x
    turn = 'left'
    answer = 0

    while gap > 0:

        if turn == 'left':
            if gap >= left + 1:
                gap -= (left + 1)
                left += 1
            elif gap >= left:
                gap -= left
            else:
                gap -= (left - 1)
                left -= 1

            answer += 1
            turn = 'right'

        elif turn == 'right':
            if gap >= right + 1:
                gap -= (right + 1)
                right += 1
            elif gap >= right:
                gap -= right
            else:
                gap -= (right - 1)
                right -= 1

            answer += 1
            turn = 'left'

    print(answer)
    return


for _ in range(T):
    program()
