import sys
N = int(input())
K = int(input())

if K >= N:
    print(0)
else:
    sensor = list(map(int, sys.stdin.readline().split()))
    sensor.sort()

    distance = []

    for i in range(1, N):
        distance.append(sensor[i]-sensor[i-1])

    distance.sort()

    K -= 1

    while K > 0:
        distance.pop()
        K -= 1

    print(sum(distance))
