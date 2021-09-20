from collections import deque

direction = [(-1, 0), (1, 0), (0,- 1), (0, 1), \
             (-1, -1), (-1, 1), (1, -1), (1, 1)]


def bfs(graph, visit, a, b):
    q = deque()
    q.append((a, b))
    visit[a][b] = True
    while q:
        x, y = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < h and 0 <= ny < w:
                if not visit[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visit[nx][ny] = True


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break

    island = 0
    graph = []
    visit = [[False]*w for _ in range(h)]
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if not visit[i][j] and graph[i][j] == 1:
                bfs(graph, visit, i, j)
                island += 1

    print(island)
