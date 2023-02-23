import sys
import math
from itertools import combinations
answer = 0
N = int(sys.stdin.readline())
stars = [tuple(map(float, sys.stdin.readline().split())) for _ in range(N)]
edges = []
parent = [x for x in range(N)]

for A, B in list(combinations(range(N), 2)):
    edges.append((A, B, math.sqrt((stars[A][0]-stars[B][0])**2 + (stars[A][1]-stars[B][1])**2)))

edges.sort(key=lambda x: x[2])


def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    px = find_parent(x)
    py = find_parent(y)
    parent[max(px, py)] = min(px, py)
    return


edge_count = 0
for A, B, dist in edges:
    if find_parent(A) == find_parent(B):
        continue
    union(A, B)
    edge_count += 1
    answer += dist
    if edge_count == N-1:
        break

print(answer)
