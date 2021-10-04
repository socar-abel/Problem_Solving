import sys
N, K = map(int, sys.stdin.readline().split())
number = sys.stdin.readline().strip()

stack = [number[0]]
for i in range(1,len(number)):
    if K == 0:
        stack.append(number[i:])
        break

    if stack[-1] >= number[i]:
        stack.append(number[i])
    else:
        while stack and K > 0 and stack[-1] < number[i]:
            stack.pop()
            K -= 1
        stack.append(number[i])

if K > 0:
    while K > 0:
        stack.pop()
        K -= 1

print(''.join(stack))
