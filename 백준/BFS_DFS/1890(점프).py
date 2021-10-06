from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
record = [[0 for _ in range(N)] for _ in range(N)]
record[0][0] = 1

for i in range(N):
    for j in range(N):
        dist = board[i][j]
        if i == j == N - 1:
            break
        if i + dist < N:
            record[i + dist][j] += record[i][j]
        if j + dist < N:
            record[i][j + dist] += record[i][j]

print(record[N - 1][N - 1])
