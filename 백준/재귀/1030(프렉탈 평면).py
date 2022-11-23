# 1030 프렉탈 평면
import sys
s, N, K, R1, R2, C1, C2 = map(int, sys.stdin.readline().split())
x_range = range(R1, R2+1)
y_range = range(C1, C2+1)
graph = [[0] * (C2 - C1 + 1) for _ in range(R2 - R1 + 1)]

def draw(x, y, size):
    if size <= 1:
        return
    center_size = int(size * (K/N))
    unit_size = size // N
    side_size = (size - center_size) // 2
    center_x1 = x + side_size
    center_x2 = x + size - side_size - 1
    center_y1 = y + side_size
    center_y2 = y + size - side_size - 1
    inter_x1 = max(x, R1)
    inter_x2 = min(x + size, R2)
    inter_y1 = max(y, C1)
    inter_y2 = min(y + size, C2)

    next_set = set()
    for i in range(inter_x1, inter_x2 + 1):
        for j in range(inter_y1, inter_y2 + 1):
            if center_x1 <= i <= center_x2 and center_y1 <= j <= center_y2:
                graph[i - R1][j - C1] = 1
            else:
                next_set.add(((i//unit_size)*unit_size, (j//unit_size)*unit_size))
    for nx, ny in list(next_set):
        draw(nx, ny, size//N)

draw(0, 0, N**s)

for x in graph:
    print(''.join(map(str, x)))




