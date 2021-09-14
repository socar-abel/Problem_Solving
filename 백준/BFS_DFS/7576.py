from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(M):
    graph.append(list(map(int, input().split())))

tomato = []
for a in range(M):
    for b in range(N):
        if graph[a][b] == 1 : tomato.append((a, b))

def bfs():
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque()
    for t in tomato:
        q.append(t)

    while q:
        x, y = q.popleft()
        #print('x y', x, y)
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            cost = graph[x][y] + 1

            if 0 <= nx < M and 0 <= ny < N and ( (graph[nx][ny] == 0) or (graph[nx][ny] > cost) ):
                q.append((nx, ny))
                graph[nx][ny] = cost

    answer = 0
    for a in range(M):
        for b in range(N):
            if graph[a][b] > answer : answer = graph[a][b]
            if graph[a][b] == 0: return -1

    return answer - 1

print(bfs())
