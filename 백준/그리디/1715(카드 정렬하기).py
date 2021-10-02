import sys
import heapq
N = int(input())
card = []

for _ in range(N):
    heapq.heappush(card, int(sys.stdin.readline()))

answer = 0

while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)

    answer += (first + second)
    heapq.heappush(card, (first + second))

print(answer)

