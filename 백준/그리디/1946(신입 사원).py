import sys
T = int(input())
while T > 0:
    N = int(input())
    scores = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    s = sorted(scores, key=lambda x:x[0])

    minV = s[0][1]

    count = 1
    for x in s[1:]:
        if minV > x[1]:
            count += 1
            minV = x[1]

    print(count)

    T -= 1
