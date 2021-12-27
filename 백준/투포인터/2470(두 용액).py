import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

left = 0
right = N-1
answer = [arr[left], arr[right]]

while left < right:
    result = abs(arr[left] + arr[right])

    if left+1 < right and abs(arr[left+1] + arr[right]) < result:
        left += 1
    elif left < right-1 and abs(arr[left] + arr[right-1]) < result:
        right -= 1
    else:
        if result < abs(sum(answer)):
            answer = [arr[left], arr[right]]
        left += 1
        right -= 1

print(answer[0], answer[1])
