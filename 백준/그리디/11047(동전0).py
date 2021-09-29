import sys
N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]

answer = 0

while K > 0:

    i = 0
    while i < len(coin) and coin[i] <= K:
        i += 1

    answer += K // coin[i-1]
    K %= coin[i-1]

print(answer)
