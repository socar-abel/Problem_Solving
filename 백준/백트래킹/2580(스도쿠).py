import sys
graph = []
blank = []
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))


def dfs(idx):
    if idx == len(blank):
        return True
    x, y = blank[idx]

    flag = False
    for n in range(1, 10):
        if checkRow(x, y, n) and checkCol(x, y, n) and checkBox(x, y, n):
            flag = True
            graph[x][y] = n
            if not dfs(idx+1):
                graph[x][y] = 0
                flag = False

    return True if flag else False


def checkRow(x, y, n):
    for i in range(9):
        if i != y and graph[x][i] == n:
            return False
    return True


def checkCol(x, y, n):
    for i in range(9):
        if x != i and graph[i][y] == n:
            return False
    return True


def checkBox(x, y, n):
    a = 3 * (x//3)
    b = 3 * (y//3)
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            if (i, j) != (x, y) and graph[i][j] == n:
                return False
    return True


dfs(0)
for i in range(9):
    for j in range(9):
        print(graph[i][j], end=' ')
    print()

