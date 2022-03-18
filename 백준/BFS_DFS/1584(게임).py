from collections import deque
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
danger = []
death = []

N = int(sys.stdin.readline())
for _ in range(N):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    danger.append((X1, Y1, X2, Y2))

M = int(sys.stdin.readline())
for _ in range(M):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    death.append((X1, Y1, X2, Y2))

graph = [[0] * 501 for _ in range(501)]

for i in range(501):
    for j in range(501):
        # 위험 영역에 속한다면
        for a1, b1, a2, b2 in danger:
            if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
                graph[i][j] = 1
        # 죽음 영역에 속한다면
        for a1, b1, a2, b2 in death:
            if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
                graph[i][j] = 2


answer = 0
visit = [[False] * 501 for _ in range(501)]
q = deque()
# x좌표, y좌표, 깎인 생명
q.append((0, 0, 0))
visit[0][0] = True
can_reach = False

while q:
    x, y, minus_life = q.popleft()
    if x == 500 and y == 500:
        can_reach = True
        answer = minus_life
        break

    for d in direction:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx <= 500 and 0 <= ny <= 500 and not visit[nx][ny]:
            if graph[nx][ny] == 0:
                q.appendleft((nx, ny, minus_life))
                visit[nx][ny] = True
            elif graph[nx][ny] == 1:
                q.append((nx, ny, minus_life + 1))
                visit[nx][ny] = True

if can_reach:
    print(answer)
else:
    print(-1)
