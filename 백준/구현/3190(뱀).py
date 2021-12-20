import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

graph = [[0] * N for _ in range(N)]

# 사과 설정
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1

L = int(sys.stdin.readline())
curve = deque()
for _ in range(L):
    X, C = sys.stdin.readline().split()
    curve.append((int(X), C))

# 게임 시작
x = 0
y = 0
snake = deque([(0, 0)])
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
time = 1
d = 0
graph[x][y] = -1 # 뱀

while True:
    #print('x y',x,y)
    nx = x + direction[d][0]
    ny = y + direction[d][1]

    # 맵 안에 들어온 경우
    if 0 <= nx < N and 0 <= ny < N:
        # 사과를 먹을 경우
        if graph[nx][ny] == 1:
            x = nx
            y = ny
            graph[nx][ny] = -1
            snake.append((nx, ny))
        # 사과를 안먹을 경우
        elif graph[nx][ny] == 0:
            x = nx
            y = ny
            graph[nx][ny] = -1
            snake.append((nx, ny))
            # 꼬리를 자름
            tail = snake[0]
            graph[tail[0]][tail[1]] = 0
            snake.popleft()

        # 자기 몸에 부딪힐 경우
        elif graph[nx][ny] == -1:
            print(time)
            break
    # 맵 밖에 나갈 경우
    else:
        print(time)
        break

    if curve and time == curve[0][0]:
        if curve[0][1] == 'L':
            d = (d-1) % 4
        elif curve[0][1] == 'D':
            d = (d+1) % 4
        curve.popleft()

    time += 1
