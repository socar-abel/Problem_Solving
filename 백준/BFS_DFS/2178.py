from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input()))

def bfs(x, y):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(x, y)])
    while q:
        now = q.popleft()
        for i in range(4):
            nx = now[0] + direction[i][0]
            ny = now[1] + direction[i][1]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 0 and graph[nx][ny] == 1:
                graph[nx][ny] = graph[now[0]][now[1]] + 1
                q.append((nx, ny))


bfs(0, 0)
print(graph[N-1][M-1])

