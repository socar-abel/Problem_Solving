import sys
n, m = map(int, sys.stdin.readline().split())
money = list(map(int, sys.stdin.readline().split()))

window = 0
for i in range(m):
    window += money[i]

answer = window
for i in range(m, n):
    window -= money[i-m]
    window += money[i]
    answer = max(answer, window)

print(answer)
