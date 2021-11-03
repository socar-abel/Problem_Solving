import sys
given = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []

i = 0
while i < len(given):
    stack += given[i]
    if len(stack) >= len(bomb) and "".join(stack[-len(bomb):]) == bomb:
       for _ in range(len(bomb)): stack.pop()
    i+=1

if not stack: print("FRULA")
else:
    print("".join(stack))
