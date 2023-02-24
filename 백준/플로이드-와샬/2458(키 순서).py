import sys
INF = 987654321
N, M = map(int, sys.stdin.readline().split())
distance = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    distance[A][B] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            distance[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distance[i][k] + distance[k][j] < distance[i][j]:
                distance[i][j] = 1

answer = 0
for x in range(1, N+1):
    count = 0
    for y in range(1, N+1):
        if distance[x][y] == 1:
            count += 1
        if distance[y][x] == 1:
            count += 1
    if count == N-1:
        answer += 1

print(answer)

