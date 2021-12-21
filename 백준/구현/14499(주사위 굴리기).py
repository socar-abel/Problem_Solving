import sys
N, M, x, y, K = map(int, sys.stdin.readline().split())
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

cmd = list(map(int, sys.stdin.readline().split()))

dice = [-1, 0, 0, 0, 0, 0, 0] # default, 1~6
top = 1
east = 3
south = 5
direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]  # default, 동, 서, 북, 남

for c in cmd:
    nx = x + direction[c][0]
    ny = y + direction[c][1]

    # 맵 안의 범위에서.
    if 0 <= nx < N and 0 <= ny < M:
        # 굴러간다
        t, e, s = top, east, south
        # 동
        if c == 1:
            top = 7 - e
            east = t
            south = s
        # 서
        elif c == 2:
            top = e
            east = 7 - t
            south = s
        # 북
        elif c == 3:
            top = s
            east = e
            south = 7 - t
        # 남
        elif c == 4:
            top = 7 - s
            east = e
            south = t

        bottom = 7 - top
        # 이동한 칸이 0 이면
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[bottom]
        # 이동한 칸이 0이 아니면
        else:
            dice[bottom] = graph[nx][ny]
            graph[nx][ny] = 0

        x = nx
        y = ny
        print(dice[top])

    # 바깥으로 나갈 경우
    else:
        continue
