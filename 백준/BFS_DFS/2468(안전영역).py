import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = []
height = []

for _ in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    graph.append(i)
    height += i

height = sorted(list(set(height)))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(a, b, water, visit):
    result = 0

    q = deque()
    q.append((a, b))
    visit[a][b] = True

    while q:
        x, y = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > water and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))


land = 1

for water in height:
    count = 0
    visit = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] > water and not visit[i][j]:
                bfs(i, j, water, visit)
                count += 1

    land = max(land, count)

print(land)
   
   
# 두번째 풀었을 때의 풀이   
   
from collections import deque
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(sys.stdin.readline())
graph = []
maxHeight = 0
maxArea = 0

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    maxHeight = max(maxHeight, max(row))


def bfs(waterHeight):
    area = 0
    visit = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 아직 방문하지 않은 영역이면 BFS 탐색
            if not visit[i][j] and graph[i][j] > waterHeight:
                q = deque()
                q.append((i, j))
                visit[i][j] = True
                while q:
                    x, y = q.popleft()
                    for d in direction:
                        nx = x + d[0]
                        ny = y + d[1]
                        if (0 <= nx < N and 0 <= ny < N) and (not visit[nx][ny]) and (graph[nx][ny] > waterHeight):
                            q.append((nx, ny))
                            visit[nx][ny] = True
                area += 1
    return area


for water in range(maxHeight+1):
    tempArea = bfs(water)
    maxArea = max(maxArea, tempArea)

print(maxArea)

