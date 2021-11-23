import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
answer = 0

direction = [(-1,0), (0,1), (1,0), (0,-1)]  # 북 동 남 서
clean = [[False] * M for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def robotCleaner(x, y, d):
    #print('x y',x,y)
    if not clean[x][y]:
        clean[x][y] = True
        global answer
        answer += 1

    dCheck = 0
    for _ in range(4):
        nextD = d - 1
        if nextD == -5:
            nextD = 3

        nx = x + direction[nextD][0]
        ny = y + direction[nextD][1]

        # 2-a
        if 0 <= nx < N and 0 <= ny < M and not clean[nx][ny] and graph[nx][ny] == 0:
            robotCleaner(nx, ny, nextD)
            return

        dCheck += 1
        d = nextD

    if dCheck == 4:
        bx = x - direction[nextD][0]
        by = y - direction[nextD][1]
        if not graph[bx][by] == 1:
            robotCleaner(bx,by,nextD)
        else:
            return


robotCleaner(r,c,d)
print(answer)

