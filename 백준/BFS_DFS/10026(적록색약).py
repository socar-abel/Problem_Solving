import sys
sys.setrecursionlimit(1000000)
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))

d = [(-1,0),(1,0),(0,-1),(0,1)]
visited1 = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]

def dfs1(x, y, color):  # 일반인
    visited1[x][y] = True
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]

        if 0 <= nx < N and 0 <= ny < N and not visited1[nx][ny] and graph[nx][ny] == color:
            dfs1(nx, ny, color)

def dfs2(x, y, color):  # 적록색약
    visited2[x][y] = True
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if color == 'B':
            if 0 <= nx < N and 0 <= ny < N and not visited2[nx][ny] and graph[nx][ny] == color:
                dfs2(nx, ny, color)
        else:
            if 0 <= nx < N and 0 <= ny < N and not visited2[nx][ny] and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                dfs2(nx, ny, color)

count1, count2 = 0, 0

for a in range(N):
    for b in range(N):
        if not visited1[a][b]: dfs1(a, b, graph[a][b]); count1 += 1;
        if not visited2[a][b]: dfs2(a, b, graph[a][b]); count2 += 1;

print(count1, count2)



