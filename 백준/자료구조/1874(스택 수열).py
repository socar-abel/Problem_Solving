import sys
N = int(sys.stdin.readline())
standard = []
stack = []
answer = []

for _ in range(N):
    standard.append(int(sys.stdin.readline()))

j = 0
for i in range(1, N+1):
    stack.append(i)
    answer.append('+')
    while stack and (stack[-1] == standard[j]):
        stack.pop()
        answer.append('-')
        j += 1


if not stack:
    for a in answer:
        print(a)
else:
    print("NO")
