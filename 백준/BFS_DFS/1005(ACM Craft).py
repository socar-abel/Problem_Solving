from collections import deque
import copy
import sys
T = int(sys.stdin.readline())


def program():
    N, K = map(int, sys.stdin.readline().split())
    time = [-1]
    inputTime = list(map(int, sys.stdin.readline().split()))
    time = time + inputTime
    graph = [[] for _ in range(N+1)]
    cost = copy.deepcopy(time)
    visit = [False] * (N+1)
    inDegree = [0] * (N+1)
    start = []
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        inDegree[Y] += 1
    W = int(sys.stdin.readline())

    for i in range(1, N+1):
        if inDegree[i] == 0:
            start.append(i)

    q = deque()
    for i in start:
        q.append((i, time[i]))

    while q:
        now, t = q.popleft()

        for x in graph[now]:
            if not visit[x]:
                cost[x] = t + time[x]
                visit[x] = True
            else:
                cost[x] = max(cost[x], t + time[x])

            inDegree[x] -= 1
            if inDegree[x] == 0:
                q.append((x, cost[x]))

    print(cost[W])


for _ in range(T):
    program()
    
