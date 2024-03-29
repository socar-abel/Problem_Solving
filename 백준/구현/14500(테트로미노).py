import sys
N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

blocks = [
    # 1번 모양
    [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)],
    # 2번 모양
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # 3번 모양 - 회전
    [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (-1, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 0)],
    # 3번 모양 - 좌우 대칭
    [(0, 0), (0, 1), (-1, 1), (-2, 1)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (1, 0), (2, 0)], [(0, 0), (0, 1), (0, 2), (1, 2)],
    # 4번 모양 - 회전
    [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    # 4번 모양 - 좌우 대칭
    [(0, 0), (-1, 0), (-1, 1), (-2, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)],
    # 5번 모양
    [(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)], [(0, 0), (0, 1), (-1, 1), (0, 2)], [(0, 0), (0, 1), (-1, 1), (1, 1)]]

answer = 0

for block in blocks:
    for x in range(N):
        for y in range(M):
            in_the_graph = True
            temp_sum = 0
            for b in block:
                nx = x + b[0]
                ny = y + b[1]
                # 그래프 범위 내에 들었으면
                if (0 <= nx < N) and (0 <= ny < M):
                    temp_sum += graph[nx][ny]
                # 그래프 범위 내에 들지 않으면
                else:
                    in_the_graph = False
                    break
            if in_the_graph:
                answer = max(answer, temp_sum)

print(answer)

