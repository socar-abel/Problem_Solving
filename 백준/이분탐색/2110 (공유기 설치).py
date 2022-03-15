import sys
N, C = map(int, sys.stdin.readline().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()
left, right = 1, house[-1]-house[0]


# x 가 가장 인접한 거리의 최대값이 될 수 있을지.
def check(x):
    result = False
    cnt = 0
    start = 0
    for i in range(1, N):
        if house[i] - house[start] >= x:
            cnt += 1
            start = i
        if cnt == C-1:
            result = True
            break
    return result


answer = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
