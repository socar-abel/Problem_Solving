from collections import defaultdict
import sys
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_dict = defaultdict(int)
B_dict = defaultdict(int)

for i in range(n):
    temp_sum = 0
    for j in range(i, n):
        temp_sum += A[j]
        A_dict[temp_sum] += 1

for i in range(m):
    temp_sum = 0
    for j in range(i, m):
        temp_sum += B[j]
        B_dict[temp_sum] += 1

answer = 0
for key in A_dict.keys():
    if T - key in B_dict:
        answer += A_dict[key] * B_dict[T - key]

print(answer)

