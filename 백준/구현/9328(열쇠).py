from collections import deque
import sys
T = int(sys.stdin.readline())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
lower_case = list("abcdefghijklmnopqrstuvwxyz")
upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def program():
    graph = []
    entrance = []
    secretPaper = 0
    H, W = map(int, sys.stdin.readline().split())
    for _ in range(H):
        graph.append(list(sys.stdin.readline()))
    keys = list(sys.stdin.readline())

    # 빌딩 입구 탐색
    # 입구가 문인 경우는, 입구가 열쇠인 경우를 발견한다면 다시 고려해줘야 한다.
    doorEntrance = []
    for i in range(H):
        for j in range(W):
            # 가장자리인 경우
            if (i in [0, H - 1]) or (j in [0, W - 1]):
                # 빈 공간이 입구인 경우
                if graph[i][j] == '.':
                    entrance.append((i, j))
                # 문이 입구인 경우
                elif graph[i][j] in upper_case:
                    # 열쇠로 열 수 있는 문인 경우
                    if graph[i][j].lower() in keys:
                        graph[i][j] = '.'
                        entrance.append((i, j))
                    # 열 수 없는 문인 경우
                    else:
                        doorEntrance.append((i, j))
                # 문서가 입구인 경우
                elif graph[i][j] == '$':
                    secretPaper += 1
                    graph[i][j] = '.'
                    entrance.append((i, j))
                # 열쇠가 입구인 경우
                elif graph[i][j] in lower_case:
                    key = graph[i][j]
                    if not key in keys:
                        keys.append(key)
                    graph[i][j] = '.'
                    entrance.append((i, j))

    # 열 수 있는 문인지 다시 한번 고려
    for x, y in doorEntrance:
        if graph[x][y].lower() in keys:
            graph[x][y] = '.'
            entrance.append((x, y))

    # 입구 마다 BFS 탐색. 새로운 열쇠를 얻었으면 다시 탐색.
    i = 0
    length = len(entrance)
    while i < length:
        visit = [[False]*W for _ in range(H)]
        findKey = False
        a, b = entrance[i]
        q = deque()
        q.append((a, b))
        visit[a][b] = True
        while q:
            x, y = q.popleft()
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < H and 0 <= ny < W and not visit[nx][ny]:
                    # 빈 공간
                    if graph[nx][ny] == '.':
                        q.append((nx, ny))
                        visit[nx][ny] = True
                    # 문서
                    elif graph[nx][ny] == '$':
                        q.append((nx, ny))
                        visit[nx][ny] = True
                        secretPaper += 1
                        graph[nx][ny] = '.'
                    # 열쇠
                    elif graph[nx][ny] in lower_case:
                        q.append((nx, ny))
                        visit[nx][ny] = True
                        key = graph[nx][ny]
                        # 없던 키를 새로 발견한거라면
                        if not key in keys:
                            keys.append(key)
                            findKey = True
                            # 그런데 그 키로 다른 입구가 열릴 수 있다면
                            for e1, e2 in doorEntrance:
                                if key == graph[e1][e2].lower():
                                    length += 1
                                    entrance.append((e1, e2))

                        graph[nx][ny] = '.'
                    # 열 수 있는 문
                    elif (graph[nx][ny] in upper_case) and (graph[nx][ny].lower() in keys):
                        q.append((nx, ny))
                        visit[nx][ny] = True
                        graph[nx][ny] = '.'

        if findKey:
            i = 0
        else:
            i += 1
    print(secretPaper)


for _ in range(T):
    program()
