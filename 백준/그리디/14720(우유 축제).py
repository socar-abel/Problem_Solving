import sys
N = int(sys.stdin.readline())
store = list(map(int, sys.stdin.readline().split()))

now = 0
answer = 0
for milk in store:
    if now == milk:
        answer += 1
        now = (now + 1) % 3

print(answer)
