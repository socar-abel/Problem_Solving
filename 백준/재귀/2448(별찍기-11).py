import sys
import math
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
k = int(math.log2((N//3)))
tree = [[' '] * (2*N - 1) for _ in range(N+1)]


def draw_tree(x, y1, y2):
    if not ((0 <= x <= N) and (0 <= y1 < 2*N - 1) and (0 <= y2 < 2*N - 1)):
        return

    # 최소 삼각형인 경우
    if y2 - y1 == 4:
        for i in range(5):
            tree[x][y1 + i] = '*'
        tree[x-1][y1+1] = '*'
        tree[x-1][y2-1] = '*'
        tree[x-2][y1 + (y2-y1)//2] = '*'
        return

    # 최소 삼각형이 아닌 경우 재귀 수행
    # 23
    half = (y2 - y1) // 2
    draw_tree(x, y1, y1 + half - 1)
    draw_tree(x, y2 - half + 1, y2)
    n = (y2 - y1 + 2) // 2
    # 11
    quarter = (half - 1) // 2
    draw_tree(x - n//2, y1 + quarter + 1, y2 - quarter - 1)


draw_tree(N, 0, len(tree[0]) - 1)
for t in tree[1:]:
    print(''.join(t))
