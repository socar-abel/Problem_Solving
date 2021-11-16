import sys
N, K = map(int, sys.stdin.readline().split())

ice = [0] * (10**6+1)
for _ in range(N):
    g, x = map(int, sys.stdin.readline().split())
    ice[x] = g

answer = 0
window = 0

for i in range(2*K+1):
    if i > 10**6:
        print(window)
        exit(0)
    window += ice[i]

answer = max(answer, window)

for i in range(2*K+1, 10**6 + 1):
    window = window + ice[i] - ice[i - 2*K - 1]
    answer = max(answer, window)

print(answer)
