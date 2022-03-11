import sys
sys.setrecursionlimit(10**6)
V, E = map(int, sys.stdin.readline().split())
parent = [x for x in range(V+1)]
edges = []

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A, B, C))


def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]


def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


answer = 0
edges.sort(key=lambda x: x[2])

for edge in edges:
    x, y, cost = edge[0], edge[1], edge[2]
    # 사이클을 만들면 무시
    if find_parent(x) == find_parent(y):
        continue

    union(x, y)
    answer += cost


print(answer)
