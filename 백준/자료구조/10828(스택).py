import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    c = sys.stdin.readline().split()
    if c[0] == "push":
        stack.append(c[1])
    elif c[0] == "pop":
        if not stack:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif c[0] == "size":
        print(len(stack))
    elif c[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif c[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])

