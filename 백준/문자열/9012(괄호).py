import sys
T = int(sys.stdin.readline())

for _ in range(T):
    given = sys.stdin.readline().strip()
    stack = [given[0]]

    for x in given[1:]:
        if stack and stack[-1] == '(' and x == ')':
            stack.pop()
        else: stack.append(x)

    if stack: print("NO")
    else: print("YES")
