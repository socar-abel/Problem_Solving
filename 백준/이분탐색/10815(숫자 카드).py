import sys
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

cards.sort()


def check(n):
    left = 0
    right = N-1

    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == n:
            print(1, end=' ')
            return
        elif cards[mid] < n:
            left = mid + 1
        elif cards[mid] > n:
            right = mid - 1
    print(0, end=' ')


for x in numbers:
    check(x)
