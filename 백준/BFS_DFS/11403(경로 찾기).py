from collections import deque
import sys
N = int(sys.stdin.readline())
graph = []
answer = [[0]*N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    visit = [False] * N
    q = deque()
    q.append(i)

    while q:
        now = q.popleft()

        for k in range(N):
            if not visit[k] and graph[now][k] == 1:
                q.append(k)
                visit[k] = True
                answer[i][k] = 1


for i in range(N):
    for j in range(N):
        print(answer[i][j], end=' ')
    print()
