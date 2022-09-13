import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
parent = [x for x in range(n)]


def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    px = find_parent(x)
    py = find_parent(y)
    if px <= py:
        parent[py] = px
    else:
        parent[px] = py


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

answer = 0
for i in range(m):
    a, b = arr[i]
    temp_parent = []

    if find_parent(a) == find_parent(b):
        answer = i+1
        break
    else:
        union(a, b)

print(answer)

