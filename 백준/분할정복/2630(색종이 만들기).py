import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0


def is_square(x, y, size):
    color = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != color:
                return False
    return True


def recursion(x, y, size):
    global white, blue

    if is_square(x, y, size):
        if graph[x][y] == 0:
            white += 1
        else:
            blue += 1
        return

    recursion(x, y, size//2)
    recursion(x + size//2, y, size//2)
    recursion(x, y + size//2, size//2)
    recursion(x + size//2, y + size//2, size//2)
    return


recursion(0, 0, N)
print(white)
print(blue)
