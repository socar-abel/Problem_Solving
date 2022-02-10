from itertools import product
import copy
import sys
N, M = map(int, sys.stdin.readline().split())
board = []
cctv = []
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상, 좌, 하, 우

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if board[i][j] in range(1, 6):
            # 좌표, 종류
            cctv.append((i, j, board[i][j]))

product_candidate = [[0, 1, 2, 3] for _ in range(len(cctv))]
cctv_direction_case = list(product(*product_candidate))


def checkBlindSpot(direction_case):
    graph = copy.deepcopy(board)
    for idx in range(len(cctv)):
        x, y, t = cctv[idx]
        d = direction_case[idx]
        if t == 1:
            while (0 <= x < N and 0 <= y < M) and (graph[x][y] != 6):
                if graph[x][y] == 0:
                    graph[x][y] = '#'
                x = x + direction[d][0]
                y = y + direction[d][1]
        elif t == 2:
            x2, y2 = x, y
            # 방향 1
            while (0 <= x < N and 0 <= y < M) and (graph[x][y] != 6):
                if graph[x][y] == 0:
                    graph[x][y] = '#'
                x = x + direction[d][0]
                y = y + direction[d][1]
            # 방향 2
            while (0 <= x2 < N and 0 <= y2 < M) and (graph[x2][y2] != 6):
                if graph[x2][y2] == 0:
                    graph[x2][y2] = '#'
                x2 = x2 + direction[(d+2) % 4][0]
                y2 = y2 + direction[(d+2) % 4][1]
        elif t == 3:
            x2, y2 = x, y
            # 방향 1
            while (0 <= x < N and 0 <= y < M) and (graph[x][y] != 6):
                if graph[x][y] == 0:
                    graph[x][y] = '#'
                x = x + direction[d][0]
                y = y + direction[d][1]
            # 방향 2
            while (0 <= x2 < N and 0 <= y2 < M) and (graph[x2][y2] != 6):
                if graph[x2][y2] == 0:
                    graph[x2][y2] = '#'
                x2 = x2 + direction[(d + 1) % 4][0]
                y2 = y2 + direction[(d + 1) % 4][1]
        elif t == 4:
            x2, y2 = x, y
            x3, y3 = x, y
            # 방향 1
            while (0 <= x < N and 0 <= y < M) and (graph[x][y] != 6):
                if graph[x][y] == 0:
                    graph[x][y] = '#'
                x = x + direction[d][0]
                y = y + direction[d][1]
            # 방향 2
            while (0 <= x2 < N and 0 <= y2 < M) and (graph[x2][y2] != 6):
                if graph[x2][y2] == 0:
                    graph[x2][y2] = '#'
                x2 = x2 + direction[(d + 1) % 4][0]
                y2 = y2 + direction[(d + 1) % 4][1]
            # 방향 3
            while (0 <= x3 < N and 0 <= y3 < M) and (graph[x3][y3] != 6):
                if graph[x3][y3] == 0:
                    graph[x3][y3] = '#'
                x3 = x3 + direction[(d + 3) % 4][0]
                y3 = y3 + direction[(d + 3) % 4][1]
        elif t == 5:
            x2, y2 = x, y
            x3, y3 = x, y
            x4, y4 = x, y
            # 방향 1
            while (0 <= x < N and 0 <= y < M) and (graph[x][y] != 6):
                if graph[x][y] == 0:
                    graph[x][y] = '#'
                x = x + direction[d][0]
                y = y + direction[d][1]
            # 방향 2
            while (0 <= x2 < N and 0 <= y2 < M) and (graph[x2][y2] != 6):
                if graph[x2][y2] == 0:
                    graph[x2][y2] = '#'
                x2 = x2 + direction[(d + 1) % 4][0]
                y2 = y2 + direction[(d + 1) % 4][1]
            # 방향 3
            while (0 <= x3 < N and 0 <= y3 < M) and (graph[x3][y3] != 6):
                if graph[x3][y3] == 0:
                    graph[x3][y3] = '#'
                x3 = x3 + direction[(d + 2) % 4][0]
                y3 = y3 + direction[(d + 2) % 4][1]
            # 방향 4
            while (0 <= x4 < N and 0 <= y4 < M) and (graph[x4][y4] != 6):
                if graph[x4][y4] == 0:
                    graph[x4][y4] = '#'
                x4 = x4 + direction[(d + 3) % 4][0]
                y4 = y4 + direction[(d + 3) % 4][1]

    answer = 0
    for a in range(N):
        for b in range(M):
            if graph[a][b] == 0:
                answer += 1
    return answer


result = 987654321
for case in cctv_direction_case:
    result = min(result, checkBlindSpot(case))

print(result)

