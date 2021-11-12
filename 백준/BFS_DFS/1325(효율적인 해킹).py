import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)

howManyHack = [0] * (N+1)

for i in range(1, N+1):
    visit = [False] * (N + 1)
    howMany = 1
    # BFS
    q = deque()
    q.append(i)
    visit[i] = True
    while q:
        now = q.popleft()
        for x in graph[now]:
            if not visit[x]:
                q.append(x)
                howMany += 1
                visit[x] = True
    howManyHack[i] = howMany

#print(howManyHack)
answer = ""
for i in range(1, N+1):
    if howManyHack[i] == max(howManyHack):
        answer += str(i)+" "

print(answer[:-1])
