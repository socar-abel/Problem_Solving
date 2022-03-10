import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = 987654321
distance = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    # 여기를 주의해서 입력받아야 함
    distance[a][b] = min(distance[a][b], c)

for i in range(1, N+1):
    distance[i][i] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if distance[a][b] == INF:
            print(0, end=' ')
        else:
            print(distance[a][b], end=' ')
    print()
