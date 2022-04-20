from collections import deque
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, sys.stdin.readline().split())
graph = []
coin = []
answer = 11

for i in range(N):
    input_list = list(sys.stdin.readline().strip())
    graph.append(input_list)
    for j in range(M):
        if input_list[j] == 'o':
            coin.append((i, j))


def out(c):
    return True if not(0 <= c[0] < N and 0 <= c[1] < M) else False


q = deque()
q.append((coin[0], coin[1], 0))

while q:
    coin1, coin2, cnt = q.popleft()
    if out(coin1) and not out(coin2):
        answer = min(answer, cnt)
        break
    if not out(coin1) and out(coin2):
        answer = min(answer, cnt)
        break
    if out(coin1) and out(coin2):
        continue
    if cnt == 10:
        continue

    for d in direction:
        nx1 = coin1[0] + d[0]
        ny1 = coin1[1] + d[1]
        nx2 = coin2[0] + d[0]
        ny2 = coin2[1] + d[1]

        if 0 <= nx1 < N and 0 <= ny1 < M and graph[nx1][ny1] == '#':
            nx1, ny1 = coin1[0], coin1[1]
        if 0 <= nx2 < N and 0 <= ny2 < M and graph[nx2][ny2] == '#':
            nx2, ny2 = coin2[0], coin2[1]

        q.append(((nx1, ny1), (nx2, ny2), cnt + 1))


if answer == 11:
    print(-1)
else:
    print(answer)


