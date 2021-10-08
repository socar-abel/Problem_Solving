#Pypy로 제출하면 통과 됨

from collections import defaultdict
import sys
N, d, k, c = map(int, sys.stdin.readline().split())

belt = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == c : coupon = True
    belt.append(x)

belt += belt[:k-1]
answer = 0
chobab = defaultdict(int)
kind = 0

for i in range(k):
    if chobab[belt[i]] == 0:
        kind += 1
    chobab[belt[i]] += 1


for start in range(k, len(belt)):

    if chobab[belt[start-k]] == 1:
        chobab[belt[start-k]] -= 1
        kind -= 1
    elif chobab[belt[start-k]] > 1:
        chobab[belt[start-k]] -= 1

    if chobab[belt[start]] == 0:
        chobab[belt[start]] += 1
        kind += 1
    else:
        chobab[belt[start]] += 1

    if chobab[c] == 0:
        answer = max(answer, kind + 1)
    else:
        answer = max(answer, kind)

print(answer)

