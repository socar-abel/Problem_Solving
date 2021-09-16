from collections import deque

N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input())))

# for x in graph:
#     print(x)

houses = []


def bfs(a, b):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((a, b))
    count = 1
    visited[a][b] = True
    #print(graph[0][2])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if 0 <= nx < N and 0 <= ny < N and (visited[nx][ny] == False) and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count

candidate = []

for a in range(N):
    for b in range(N):
        if graph[a][b] == 1 and not visited[a][b]:
            candidate.append(bfs(a, b))

candidate.sort()
print(len(candidate))
for x in candidate:
    print(x)
