import sys
N, M = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))
answer = 0
left, right = 0, 10**9

while left <= right:
    mid = (left + right) // 2
    temp_blue = 1
    temp_lecture = 0
    flag = True
    for lecture in lectures:
        if temp_lecture + lecture <= mid:
            temp_lecture += lecture
        else:
            if lecture > mid:
                flag = False
                break
            temp_blue += 1
            temp_lecture = lecture
        if temp_blue > M:
            flag = False
            break
    if flag:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
