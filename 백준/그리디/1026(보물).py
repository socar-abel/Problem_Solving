import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for i in range(len(A)):
    answer += A[i]*B[i]

print(answer)
