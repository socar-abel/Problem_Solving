import sys
N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

end = 0
interval_sum = 0
answer = N+1

for start in range(N):
    while end < N and interval_sum < S:
        interval_sum += data[end]
        end += 1

    if interval_sum >= S:
        answer = min(answer, end-start)

    interval_sum -= data[start]

if answer == N+1:
    print(0)
else:
    print(answer)
