import sys
import copy
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = []
startRed = (0, 0)
startBlue = (0, 0)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))
    for j in range(M):
        if graph[i][j] == 'R':
            graph[i][j] = '.'
            startRed = (i, j)
        elif graph[i][j] == 'B':
            graph[i][j] = '.'
            startBlue = (i, j)


# 보드 기울이기
# 예를들어 R B 순으로 있는데 오른쪽으로 기울인다면 B가 우선순위가 되어야 한다.
def move(red, blue, d):
    board = copy.deepcopy(graph)
    board[red[0]][red[1]] = 'R'
    board[blue[0]][blue[1]] = 'B'
    stopRed = False
    stopBlue = False
    priority = ''
    gap = (red[0]-blue[0], red[1]-blue[1])

    # 상 하 좌 우
    if d == 0:
        if gap[0] > 0:
            priority = 'BLUE'
        else:
            priority = 'RED'
    elif d == 1:
        if gap[0] > 0:
            priority = 'RED'
        else:
            priority = 'BLUE'
    elif d == 2:
        if gap[1] > 0:
            priority = 'BLUE'
        else:
            priority = 'RED'
    elif d == 3:
        if gap[1] > 0:
            priority = 'RED'
        else:
            priority = 'BLUE'

    while True:
        if stopRed and stopBlue:
            break
        nRed = red
        nBlue = blue

        # 먼저 현재 구슬자리를 비워놓음
        if not stopRed:
            board[red[0]][red[1]] = '.'
            nRed = red[0] + direction[d][0], red[1] + direction[d][1]
        if not stopBlue:
            board[blue[0]][blue[1]] = '.'
            nBlue = blue[0] + direction[d][0], blue[1] + direction[d][1]

        # 우선권이 빨강일 때
        if priority == 'RED':
            # 빨강 처리
            if not stopRed:
                nextRedValue = board[nRed[0]][nRed[1]]
                if nextRedValue == '.':
                    red = nRed
                    board[red[0]][red[1]] = 'R'
                elif nextRedValue == '#':
                    board[red[0]][red[1]] = 'R'
                    stopRed = True
                elif nextRedValue == 'O':
                    red = 'GOAL'
                    stopRed = True
                elif nextRedValue == 'B':
                    board[red[0]][red[1]] = 'R'
                    stopRed = True
            # 파랑 처리
            if not stopBlue:
                nextBlueValue = board[nBlue[0]][nBlue[1]]
                if nextBlueValue == '.':
                    blue = nBlue
                    board[blue[0]][blue[1]] = 'B'
                elif nextBlueValue == '#':
                    board[blue[0]][blue[1]] = 'B'
                    stopBlue = True
                elif nextBlueValue == 'O':
                    blue = 'GOAL'
                    stopBlue = True
                elif nextBlueValue == 'R':
                    board[blue[0]][blue[1]] = 'B'
                    stopBlue = True
        # 우선권이 파랑일때
        elif priority == 'BLUE':
            # 파랑 처리
            if not stopBlue:
                nextBlueValue = board[nBlue[0]][nBlue[1]]
                if nextBlueValue == '.':
                    blue = nBlue
                    board[blue[0]][blue[1]] = 'B'
                elif nextBlueValue == '#':
                    board[blue[0]][blue[1]] = 'B'
                    stopBlue = True
                elif nextBlueValue == 'O':
                    blue = 'GOAL'
                    stopBlue = True
                elif nextBlueValue == 'R':
                    board[blue[0]][blue[1]] = 'B'
                    stopBlue = True
            # 빨강 처리
            if not stopRed:
                nextRedValue = board[nRed[0]][nRed[1]]
                if nextRedValue == '.':
                    red = nRed
                    board[red[0]][red[1]] = 'R'
                elif nextRedValue == '#':
                    board[red[0]][red[1]] = 'R'
                    stopRed = True
                elif nextRedValue == 'O':
                    red = 'GOAL'
                    stopRed = True
                elif nextRedValue == 'B':
                    board[red[0]][red[1]] = 'R'
                    stopRed = True

    return red, blue


turn = 0
answer = 100
# BFS 시작 (빨간 공 위치, 파란 공 위치, 턴 횟수, 빨강 방문, 파랑 방문)
visit = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q = deque()
q.append(( (startRed[0], startRed[1]), (startBlue[0], startBlue[1]), turn))
visit[startRed[0]][startRed[1]][startBlue[0]][startBlue[1]] = True
go = True

while q:
    nowRed, nowBlue, t = q.popleft()
    if t >= 10:
        break
    # 상하좌우 탐색
    for i in range(4):
        nextRed, nextBlue = move(nowRed, nowBlue, i)
        if nextRed == 'GOAL' and nextBlue != 'GOAL':
            answer = min(answer, t + 1)
            go = False
            break
        elif nextRed == 'GOAL' and nextBlue == 'GOAL':
            continue
        elif nextRed != 'GOAL' and nextBlue != 'GOAL':
            if not visit[nextRed[0]][nextRed[1]][nextBlue[0]][nextBlue[1]]:
                q.append((nextRed, nextBlue, t + 1))
                visit[nextRed[0]][nextRed[1]][nextBlue[0]][nextBlue[1]] = True
        elif nextRed != 'GOAL' and nextBlue == 'GOAL':
            continue

    if not go:
        break

if answer == 100:
    print(-1)
else:
    print(answer)
