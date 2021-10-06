import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

end = 0
interval_sum = 0
answer = 0

for start in range(N):
    while end < N and interval_sum < M:
        interval_sum += A[end]
        end += 1

    if interval_sum == M:
        answer += 1

    interval_sum -= A[start]

print(answer)
