import sys
K, N = map(int, sys.stdin.readline().split())
wire = []

for _ in range(K):
    wire.append(int(sys.stdin.readline()))


def check(length):
    canMake = 0
    for w in wire:
        canMake += (w // length)
    if canMake >= N:
        return True
    else:
        return False


left = 1
right = max(wire)

answer = 0
while left <= right:
    mid = (left+right) // 2
    if check(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1


print(answer)
