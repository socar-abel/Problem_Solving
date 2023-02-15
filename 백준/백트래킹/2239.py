import sys
import copy

graph = []
zero = []
answer = []

for _ in range(9):
    graph.append(list(map(int, sys.stdin.readline().strip())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append((i, j))


def is_validate(x, y, n):
    result = True
    section_x = x - (x % 3)
    section_y = y - (y % 3)
    for i in range(section_x, section_x + 3):
        for j in range(section_y, section_y + 3):
            if graph[i][j] == n:
                result = False
                break
    for i in range(9):
        if graph[x][i] == n or graph[i][y] == n:
            result = False
            break
    return result


def dfs(idx):
    x, y = zero[idx]
    for n in range(1, 10):
        if is_validate(x, y, n):
            graph[x][y] = n
            if idx == len(zero) - 1:
                for i in range(9):
                    for j in range(9):
                        print(graph[i][j], end='')
                    print()
                sys.exit(0)
            else:
                dfs(idx + 1)
            graph[x][y] = 0

dfs(0)

