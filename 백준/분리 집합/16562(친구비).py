import sys
N, M, K = map(int, sys.stdin.readline().split())
cost = [0] + list(map(int, sys.stdin.readline().split()))
parent = [x for x in range(N+1)]


def findParent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = findParent(parent[x])
        return parent[x]


def union(x, y):
    px = findParent(x)
    py = findParent(y)

    if px != py:
        if px < py:
            parent[py] = px
        else:
            parent[px] = py


for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    union(v, w)

parents = set()
for p in parent[1:]:
    parents.add(p)

parent_cost = dict()
for c in range(1, N+1):
    pc = findParent(c)
    if pc not in parent_cost:
        parent_cost[pc] = cost[c]
    else:
        parent_cost[pc] = min(parent_cost[pc], cost[c])

total_cost = 0
for key in parent_cost:
    total_cost += parent_cost[key]

if total_cost > K:
    print("Oh no")
else:
    print(total_cost)
