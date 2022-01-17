from itertools import combinations
from collections import deque
import sys
graph = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
positions = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(positions, 7))
answer = 0

for _ in range(5):
    graph.append(list(sys.stdin.readline().strip()))


def checkDaSom(givenComb):
    daSom = 0
    for x, y in givenComb:
        if graph[x][y] == 'S':
            daSom += 1
    return True if daSom >= 4 else False


def checkAdjacent(givenComb):
    visit = [False]*7
    q = deque()
    q.append(givenComb[0])
    visit[0] = True

    while q:
        x, y = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if (nx, ny) in givenComb:
                nextIdx = givenComb.index((nx, ny))
                if not visit[nextIdx]:
                    q.append((nx, ny))
                    visit[nextIdx] = True

    return False if False in visit else True


for comb in combs:
    if checkDaSom(comb):
        if checkAdjacent(comb):
            answer += 1

print(answer)
