import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


def getTree(h):
    result = 0
    for t in tree:
        if h < t:
            result += (t - h)
    return result


left = 0
right = 10**9
answer = 0
while left <= right:
    mid = (left + right) // 2
    if M > getTree(mid):
        right = mid - 1
    elif M <= getTree(mid):
        answer = mid
        left = mid + 1


print(answer)

