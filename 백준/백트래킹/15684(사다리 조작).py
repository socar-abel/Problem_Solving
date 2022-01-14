from itertools import combinations
import copy
import sys
N, M, H = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for _ in range(H)]
positions = []
for i in range(H):
    for j in range(N):
        positions.append((i, j))

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1


def arriveItself(i, newGraph):
    x = -1
    y = i
    for _ in range(H):
        if newGraph[x+1][y] == 1:
            x, y = x+1, y+1
        elif newGraph[x+1][y-1] == 1:
            x, y = x+1, y-1
        else:
            x, y = x+1, y
    return True if y == i else False


def checkAll(newGraph):
    check = True
    for i in range(N):
        if not arriveItself(i, newGraph):
            check = False
            break
    return check


def canSatisfy(combs):
    result = False
    for comb in combs:
        newLadder = []
        overLap = False
        for c in comb:
            if graph[c[0]][c[1]] == 1:
                overLap = True
                break
            else:
                newLadder.append((c[0], c[1]))

        if overLap:
            continue

        for a, b in newLadder:
            graph[a][b] = 1

        if checkAll(graph):
            result = True

        for c, d in newLadder:
            graph[c][d] = 0

        if result:
            return True

    return result


answer = -1
for addLadderNum in range(4):
    if addLadderNum == 0:
        if checkAll(graph):
            answer = 0
            break
    else:
        combForNum = list(combinations(positions, addLadderNum))
        if canSatisfy(combForNum):
            answer = addLadderNum
            break

print(answer)

