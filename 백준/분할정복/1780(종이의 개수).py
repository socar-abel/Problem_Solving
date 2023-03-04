import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = [0, 0, 0]


def is_square(x, y, size):
    elem = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if elem != graph[i][j]:
                return False
    return True


def dfs(x, y, size):
    global answer
    if is_square(x, y, size):
        if graph[x][y] == -1:
            answer[0] += 1
        elif graph[x][y] == 0:
            answer[1] += 1
        else:
            answer[2] += 1
        return

    new_size = size//3
    for i in range(3):
        for j in range(3):
            dfs(x + new_size * i, y + new_size * j, new_size)


dfs(0, 0, N)
for a in answer:
    print(a)
