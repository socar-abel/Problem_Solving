import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

window = 0
for i in range(K):
    window += arr[i]

answer = window
for i in range(K, N):
    window = window - arr[i - K] + arr[i]
    answer = max(answer, window)

print(answer)
