import heapq
import sys
N = int(sys.stdin.readline())

q = []

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    if not q:
        for x in temp:
            heapq.heappush(q, x)
    else:
        for x in temp:
            top = q[0]
            if x < top:
                continue
            else:
                heapq.heappop(q)
                heapq.heappush(q, x)

q.sort()
print(q[0])
