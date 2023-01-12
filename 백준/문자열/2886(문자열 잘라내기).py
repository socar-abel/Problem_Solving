import sys
R, C = map(int, sys.stdin.readline().split())
strings = [''] * C

for _ in range(R):
    temp = sys.stdin.readline().strip()
    for i in range(C):
        strings[i] += temp[i]

answer = 0
for i in range(1, C):
    temp_set = set()
    for s in strings:
        temp_set.add(s[i:])
    if len(temp_set) == C:
        answer += 1
    else:
        break

print(answer)



