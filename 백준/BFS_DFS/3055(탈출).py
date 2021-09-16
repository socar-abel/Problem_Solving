# graph.append(list(input().split())) -> input().split()을 input()으로 변경하여 정답!
# 도움주신 백준 알고리즘 입문방 "내 머릿속을 시뮬레이션"님 잊지 않겠습니다.

from collections import deque
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))
water = []  # 물 좌표 리스트
hedgehog = (0, 0)  # 고슴도치 좌표
beaver = (0, 0) # 비버 집 좌표
# 좌표 세팅
# 물은 음수, 고슴도치는 양수로 뻗어나간다.
for a in range(R):
    for b in range(C):
        if graph[a][b] == '*':
            water.append((a, b))
            graph[a][b] = -1
        elif graph[a][b] == 'S':
            hedgehog = (a, b)
        elif graph[a][b] == 'D':
            beaver = (a, b)
def bfs():
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    if water:   # 물이 있다면
        q = deque()
        for w in water:
            q.append(w)  # 물 좌표 큐에 삽입
        # 물에 대해 첫번째 BFS 실행
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + d[i][0]
                ny = y + d[i][1]
                cost = graph[x][y] - 1
                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = cost
                        q.append((nx, ny))
                    elif graph[nx][ny] != '.' and graph[nx][ny] != 'D' and graph[nx][ny] != 'S'\
                    and graph[nx][ny] != 'X' and graph[nx][ny] < 0:
                        if graph[nx][ny] < cost:
                            graph[nx][ny] = cost
                            q.append((nx, ny))
    # 고슴도치에 대해 두번째 BFS 실행
    q2 = deque()
    q2.append(hedgehog)
    graph[hedgehog[0]][hedgehog[1]] = 1
    while q2:
        x, y = q2.popleft()
        for j in range(4):
            nx = x + d[j][0]
            ny = y + d[j][1]
            cost = graph[x][y] + 1
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == 'X':
                    continue
                elif graph[nx][ny] == 'D':
                    graph[nx][ny] = cost
                    q2.append((nx, ny))
                elif graph[nx][ny] != 'X' and graph[nx][ny] != 'D' and graph[nx][ny] != '.'\
                and graph[nx][ny] < 0:
                    if abs(graph[nx][ny]) > cost:
                        graph[nx][ny] = cost
                        q2.append((nx, ny))
                elif graph[nx][ny] == '.':
                    graph[nx][ny] = cost
                    q2.append((nx, ny))
bfs()
answer = graph[beaver[0]][beaver[1]]
if answer == 'D':
    print('KAKTUS')
else:
    print(answer - 1)
