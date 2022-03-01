# 오답 코드. Union 과 Find 가 명확하게 구현되어있지 않다.
# root 노드 테이블만 갱신한다고 개념이 잡혀있음.

import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

plan = list(map(int, sys.stdin.readline().split()))
parent = [x for x in range(N)]


# find
def findParent(x):
    selfParent = True
    for j in range(N):
        if graph[x][j] == 1 and j < x:
            selfParent = False
            parent[x] = findParent(j)
            return parent[x]
    if selfParent:
        return x


# union
for i in range(N):
    parent[i] = findParent(i)

root = parent[plan[0]-1]
for p in plan:
    if root != parent[p-1]:
        print("NO")
        sys.exit(0)

print("YES")
