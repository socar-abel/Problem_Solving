import sys
N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = []

a = 0; b = 0

while a < len(A) and b < len(B):
    if A[a] <= B[b]:
        C.append(A[a])
        a += 1
    else:
        C.append(B[b])
        b += 1

if a == len(A):
    C = C + B[b:]
else:
    C = C + A[a:]

for c in C:
    print(c, end = ' ')
