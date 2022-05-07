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

gems.sort()
bags.sort()

i = 0
h = []
ans = 0
for bag in bags:
    while i < N and gems[i][0] <= bag:
        heapq.heappush(h, -gems[i][1])
        i += 1
    if h:
        gem = -heapq.heappop(h)
        ans += gem

print(ans)
