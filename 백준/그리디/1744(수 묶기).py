import sys
N = int(input())
plus = []
minus = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num <= 0: minus.append(num)
    else: plus.append(num)

plus.sort(reverse=True)
minus.sort()
answer = 0

i = 0
while i < len(plus):
    if i+1 < len(plus):
        if plus[i] == 1 or plus[i+1] == 1:
            answer += (plus[i] + plus[i+1])
            i += 2
        else:
            answer += (plus[i] * plus[i + 1])
            i += 2
    else:
        answer += plus[i]
        i += 1

j = 0
while j < len(minus):
    if j+1 < len(minus):
        answer += (minus[j] * minus[j + 1])
        j += 2

    else:
        answer += minus[j]
        j += 1

print(answer)
