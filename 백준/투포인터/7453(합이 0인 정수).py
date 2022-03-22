import sys
A, B, C, D = [], [], [], []
N = int(sys.stdin.readline())

for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = dict()
CD = dict()
answer = 0

for a in A:
    for b in B:
        if a + b in AB:
            AB[a + b] += 1
        else:
            AB[a + b] = 1

for c in C:
    for d in D:
        if - (c + d) in AB:
            answer += AB[- (c + d)]

print(answer)
