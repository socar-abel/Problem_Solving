import heapq
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = [-1] * N
h = []

for i in range(N):
    a = A[i]
    # 힙이 비어있으면 그냥 삽입
    if not h:
        heapq.heappush(h, (a, i))
        continue

    top = h[0]
    if a <= top[0]:
        heapq.heappush(h, (a, i))
    else:
        while h and a > h[0][0]:
            value, idx = heapq.heappop(h)
            B[idx] = a
        heapq.heappush(h, (a, i))

for b in B:
    print(b, end=' ')
