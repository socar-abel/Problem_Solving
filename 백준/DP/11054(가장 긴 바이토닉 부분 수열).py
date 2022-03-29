import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
upDP = [1] * N
downDP = [1] * N

for i in range(1, N):
    max_value = 0
    for j in range(i):
        if A[j] < A[i]:
            max_value = max(max_value, upDP[j])
    upDP[i] += max_value

for i in reversed(range(N-1)):
    max_value = 0
    for j in range(i+1, N):
        if A[i] > A[j]:
            max_value = max(max_value, downDP[j])
    downDP[i] += max_value

dp = [x+y for x, y in zip(upDP, downDP)]
print(max(dp) - 1)
