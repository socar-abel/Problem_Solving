import sys
from collections import deque
T = int(sys.stdin.readline())

def program():
    N, Q = map(int, sys.stdin.readline().split())
    given = deque(list(map(int, sys.stdin.readline().split())))
    printer = deque([(given[i], i) for i in range(len(given))])

    out = 1
    while True:
        #print(printer)

        if max(printer, key=lambda x:x[0])[0] > printer[0][0]:
            now = printer[0]
            printer.popleft()
            printer.append(now)

        else:
            now = printer[0]
            printer.popleft()
            if now[1] == Q:
                print(out)
                break
            out += 1

for _ in range(T):
    program()


