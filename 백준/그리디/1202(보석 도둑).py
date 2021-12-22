import sys
import heapq
N, K = map(int, sys.stdin.readline().split())
gems = []
bags = []

for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    gems.append((M, V))

for _ in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)

# 가벼운 보석 순으로 정렬
gems.sort()
# 가벼운 가방 순으로 정렬
bags.sort()

candidate = []
i = 0
answer = 0
for bag in bags:
    while i < len(gems) and bag >= gems[i][0]:
        heapq.heappush(candidate, -gems[i][1])
        i += 1

    if candidate:
        maxGem = heapq.heappop(candidate)
        answer += maxGem * (-1)

print(answer)
