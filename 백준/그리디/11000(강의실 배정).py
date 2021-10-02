import sys
import heapq
N = int(input())
lecture = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

lecture.sort(key=lambda x: (x[0],x[1]))

end = []
heapq.heappush(end, lecture[0][1])
answer = 1

for lec in lecture[1:]:
    if lec[0] < end[0]:
        heapq.heappush(end, lec[1])
        answer += 1
    else:
        heapq.heappop(end)
        heapq.heappush(end, lec[1])
        answer += 0

print(answer)
