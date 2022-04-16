# 절댓값 힙
import sys
import heapq
N = int(sys.stdin.readline())
plus_heap = []
minus_heap = []
cmd = []

for _ in range(N):
    x = int(sys.stdin.readline())
    cmd.append(x)

for x in cmd:
    if x < 0:
        heapq.heappush(minus_heap, -x)
    elif x > 0:
        heapq.heappush(plus_heap, x)
    else:
        if not minus_heap and not plus_heap:
            print(0)
            continue
        if not minus_heap:
            print(plus_heap[0])
            heapq.heappop(plus_heap)
            continue
        if not plus_heap:
            print(-minus_heap[0])
            heapq.heappop(minus_heap)
            continue

        minus_top = minus_heap[0]
        plus_top = plus_heap[0]

        if plus_top < minus_top:
            print(plus_top)
            heapq.heappop(plus_heap)
        else:
            print(-minus_top)
            heapq.heappop(minus_heap)

