from collections import deque

# 전체적으로 DFS 를 사용하되, 다음으로 이동할 노드를 BFS 로 찾는다.

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

babyShark = (0, 0)
for a in range(N):
    for b in range(N):
        if graph[a][b] == 9: babyShark = (a, b)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우


# 다음으로 먹으러갈 물고기의 좌표를 찾는 bfs
def bfs(a, b, shark, visited):
    q = deque()
    q.append((a, b, 0))
    visited[a][b] = True
    fish = []   # 먹으러 갈 수 있는 물고기의 좌표들
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 빈칸(0)이거나 크기가 같은 물고기이면 지나친다.
                if graph[nx][ny] == 0 or graph[nx][ny] == shark:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
                # 상어보다 작은 물고기가 보이는 순간 큐에 그 이상 담을 필요가 없다.
                elif 0 < graph[nx][ny] < shark:
                    fish.append((nx, ny, dist + 1))

    # 다음으로 먹으러갈 물고기가 있다면
    if fish:
        # 거리, x좌표, y좌표 순으로 물고기좌표 정렬
        result = sorted(fish, key=lambda x: (x[2], x[0], x[1]))
        # 정렬된 result 의 0번째 원소가 최종 선별된 물고기
        x, y, dist = result[0][0], result[0][1], result[0][2]
        return x, y, dist  # 다음으로 먹으러 갈 물고기 좌표, 그곳까지 가는 거리

    # 없다면 None 리턴
    return None


# 아기상어가 움직일 dfs
def dfs(x, y, shark, eat, dist):    # 상어좌표, 상어크기, 몇마리 먹었는지, 거리
    # bfs 방문처리 리스트
    visited = [[False] * N for _ in range(N)]
    # 먹으러 갈 물고기의 좌표를 bfs 로 탐색
    nextFish = bfs(x, y, shark, visited)

    if not nextFish:  # 더 이상 먹으러 갈 물고기가 없으면
        print(dist);    # 여태껏 움직인 거리를 출력
        return

    else:  # 먹으러 갈 물고기가 있으면 먹으러 감
        nx, ny, d = nextFish
        graph[nx][ny] = 0  # 이동과 동시에 물고기를 먹는다
        if eat + 1 == shark:
            dfs(nx, ny, shark + 1, 0, dist + d)
        else:
            dfs(nx, ny, shark, eat + 1, dist + d)


# 아기상어가 출발하면 그 자리도 0이 되어야 함. 이 생각 못해서 헤맴..;
graph[babyShark[0]][babyShark[1]] = 0
dfs(babyShark[0], babyShark[1], 2, 0, 0)
