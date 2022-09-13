import sys
from collections import deque
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, sys.stdin.readline().split())
graph = []
visit = [[False] * M for _ in range(N)]
edges = []
temp_island_num = 1

for _ in range(N):
    graph.append((list(map(int, sys.stdin.readline().split()))))


# 섬 구분 짓기 BFS
for i in range(N):
    for j in range(M):
        if (not visit[i][j]) and graph[i][j] != 0:
            q = deque()
            q.append((i, j))
            visit[i][j] = True
            graph[i][j] = temp_island_num

            while q:
                x, y = q.popleft()

                for d in direction:
                    nx = x + d[0]
                    ny = y + d[1]

                    if (0 <= nx < N and 0 <= ny < M) and (not visit[nx][ny]) and (graph[nx][ny] != 0):
                        visit[nx][ny] = True
                        graph[nx][ny] = temp_island_num
                        q.append((nx, ny))

            temp_island_num += 1

# 최소 다리 길이 - 간선 데이터 모으기 - 완전 탐색
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            current_island_num = graph[i][j]

            for d in direction:
                x = i
                y = j
                move = 0

                while True:
                    move += 1
                    nx = x + d[0]
                    ny = y + d[1]

                    # 범위를 벗어 나거나 자기 자신을 만났다면 break
                    if (not (0 <= nx < N and 0 <= ny < M)) or (graph[nx][ny] == current_island_num):
                        break

                    if (graph[nx][ny] != 0) and (graph[nx][ny] != current_island_num):
                        if move >= 3:
                            # 출발한 섬, 도착한 섬, 이동 거리
                            edges.append((current_island_num, graph[nx][ny], move-1))
                        break

                    x = nx
                    y = ny

edges.sort(key=lambda x: x[2])

parent = [x for x in range(temp_island_num)]


def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]


def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


answer_edges = []
island_set = set()
answer = 0
n = 0
for edge in edges:
    A, B, cost = edge
    if not find_parent(A) == find_parent(B):
        union(A, B)
        answer += cost
        n += 1
        answer_edges.append(edge)

# for g in graph:
#     print(g)

# print()
# print("answer_edges", answer_edges)
# print("island_set", island_set)
# print("전체 섬 수", temp_island_num - 1)

if n == temp_island_num - 2:
    print(answer)
else:
    print(-1)

