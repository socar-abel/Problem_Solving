# pypy3로 돌려야 하고, 리스트에 알파벳을 담아가며 백트래킹하면 시간통과를 못한다. 아스키코드 연산을 사용해야 한다.
# 억지스럽긴 하지만, 코드 최적화를 배운 문제

from collections import deque
import sys
alpha = [0]*26
R, C = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
    graph.append(list(sys.stdin.readline()))


answer = 0
d = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

def dfs(x, y, cnt):
    global answer
    alpha[ord(graph[x][y])-ord('A')] = 1
    answer = max(answer, cnt)

    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0<=nx<R and 0<=ny<C and alpha[ord(graph[nx][ny])-ord('A')] == 0:
            dfs(nx, ny, cnt+1)
            alpha[ord(graph[nx][ny])-ord('A')] = 0

dfs(0, 0, 1)
print(answer)
