import sys
N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
answer = [0]
stack = [(tower[0], 1)]

for i in range(1, N):
    t = tower[i]
    if not stack:
        stack.append((t, i+1))
        answer.append(0)
        continue

    if t > stack[-1][0]:
        while stack and t > stack[-1][0]:
            stack.pop()

        if not stack:
            answer.append(0)
        else:
            answer.append(stack[-1][1])
        stack.append((t, i+1))
    else:
        answer.append(stack[-1][1])
        stack.append((t, i+1))

for a in answer:
    print(a, end=' ')
