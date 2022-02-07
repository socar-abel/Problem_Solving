import sys
N, K = map(int, sys.stdin.readline().split())
diamond = []

for _ in range(N):
    diamond.append(int(sys.stdin.readline()))

# 다이아 개수가 2 이하면 생각할 필요 x
if N <= 2:
    print(N)
    sys.exit(0)

diamond.sort()
howMany = []

right = 0
for left in range(N):
    # 차이가 K 이하면 구간에 담음
    while right < N and diamond[right] - diamond[left] <= K:
        right += 1
        change = True

    howMany.append(right - left)

#print(howMany)

maxValueToEnd = [0]*N
maxValueToEnd[N-1] = howMany[N-1]
for i in reversed(range(N-1)):
    maxValueToEnd[i] = max(howMany[i], maxValueToEnd[i+1])

#print(maxValueToEnd)
answer = 0
for i in range(N):
    if i + howMany[i] == N:
        answer = max(answer, howMany[i])
    else:
        answer = max(answer, howMany[i] + maxValueToEnd[i + howMany[i]])

print(answer)
