import sys
import heapq

N = int(sys.stdin.readline())
arr = []
leftHeap = []
rightHeap = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

where = 0
for i in range(len(arr)):
    x = arr[i]
    if where % 2 == 0:
        heapq.heappush(leftHeap, -x)
    else:
        heapq.heappush(rightHeap, x)

    if rightHeap:
        left = heapq.heappop(leftHeap)
        right = heapq.heappop(rightHeap)

        if left * (-1) > right:
            heapq.heappush(leftHeap, right * (-1))
            heapq.heappush(rightHeap, left * (-1))
        else:
            heapq.heappush(leftHeap, left)
            heapq.heappush(rightHeap, right)

        leftTop = heapq.heappop(leftHeap)
        print(leftTop * (-1))
        heapq.heappush(leftHeap, leftTop)

    else:
        leftTop = heapq.heappop(leftHeap)
        print(leftTop*(-1))
        heapq.heappush(leftHeap, leftTop)

    where += 1

