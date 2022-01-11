import sys
from itertools import combinations

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

combs = list(combinations(range(N), N//2))


def getTeamGap(teamAList):
    teamBList = []
    for x in range(N):
        if x not in teamAList:
            teamBList.append(x)

    coupleAList = list(combinations(teamAList, 2))
    coupleBList = list(combinations(teamBList, 2))
    scoreA, scoreB = 0, 0

    for a, b in coupleAList:
        scoreA += graph[a][b] + graph[b][a]

    for c, d in coupleBList:
        scoreB += graph[c][d] + graph[d][c]

    #print('gap :',abs(scoreA - scoreB))
    return abs(scoreA - scoreB)


#print('combs', combs)

answer = 987654321
for comb in combs:
    answer = min(answer, getTeamGap(comb))

print(answer)
