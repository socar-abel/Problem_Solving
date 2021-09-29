import sys
from collections import defaultdict
N = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 1
end = meetings[0][1]
for meet in meetings[1:]:
    if meet[0] >= end:
        count += 1
        end = meet[1]

print(count)
