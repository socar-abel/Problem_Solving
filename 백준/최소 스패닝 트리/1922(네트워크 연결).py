import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [x for x in range(N+1)]
edges = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])


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
for x, y, cost in edges:
    if find_parent(x) == find_parent(y):
        continue

    union(x, y)
    answer += cost

print(answer)

