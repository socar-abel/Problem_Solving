import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))


def binarySearch(x):
    left = 0
    right = len(A)-1

    while left <= right:
        mid = (left + right) // 2
        if x < A[mid]:
            right = mid - 1
        elif x > A[mid]:
            left = mid + 1
        elif x == A[mid]:
            return 1

    return 0


for x in B:
    print(binarySearch(x))
