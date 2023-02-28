import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]


def dfs(x, y, size):
    compress = True
    element = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != element:
                compress = False

    if compress:
        return str(element)
    else:
        return "(" + dfs(x, y, size//2) + dfs(x, y + size//2, size//2) + dfs(x + size//2, y, size//2) + dfs(x + size//2, y + size//2, size//2) + ")"


answer = dfs(0, 0, N)
print(answer)

