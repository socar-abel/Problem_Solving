import sys
N = int(sys.stdin.readline())

for _ in range(1):
    a, b, c = map(int, sys.stdin.readline().split())

minDP = [[0]*3 for _ in range(2)]
maxDP = [[0]*3 for _ in range(2)]

minDP[0] = [a, b, c]
maxDP[0] = [a, b, c]

if N == 1: 
    print(max(maxDP[0]), min(minDP[0]))
    exit(0)

for _ in range(1, N):
    a, b, c = map(int, sys.stdin.readline().split())

    minDP[1][0] = min(minDP[0][0], minDP[0][1]) + a
    minDP[1][1] = min(minDP[0][0], minDP[0][1], minDP[0][2]) + b
    minDP[1][2] = min(minDP[0][1], minDP[0][2]) + c

    maxDP[1][0] = max(maxDP[0][0], maxDP[0][1]) + a
    maxDP[1][1] = max(maxDP[0][0], maxDP[0][1], maxDP[0][2]) + b
    maxDP[1][2] = max(maxDP[0][1], maxDP[0][2]) + c

    minDP[0] = minDP[1][:]
    maxDP[0] = maxDP[1][:]

print(max(maxDP[1]), min(minDP[1]))
