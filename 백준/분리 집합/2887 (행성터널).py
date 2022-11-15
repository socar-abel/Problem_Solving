import sys
N = int(sys.stdin.readline())
answer = 0
stars = []
edges = []
parent = [x for x in range(N)]

for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    # (행성 번호, x, y, z)
    stars.append((i, x, y, z))

x_sorted = sorted(stars, key=lambda x: x[1])
y_sorted = sorted(stars, key=lambda x: x[2])
z_sorted = sorted(stars, key=lambda x: x[3])

for i in range(N-1):
    # (노드1, 노드2, 거리)
    edges.append((x_sorted[i][0], x_sorted[i+1][0], abs(x_sorted[i][1] - x_sorted[i+1][1])))
    edges.append((y_sorted[i][0], y_sorted[i+1][0], abs(y_sorted[i][2] - y_sorted[i+1][2])))
    edges.append((z_sorted[i][0], z_sorted[i+1][0], abs(z_sorted[i][3] - z_sorted[i+1][3])))

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    px = find_parent(x)
    py = find_parent(y)
    parent[max(px, py)] = min(px, py)

edges.sort(key=lambda x: x[2])
edge_cnt = 0

for node1, node2, dist in edges:
    if edge_cnt == N-1:
        break
    if find_parent(node1) == find_parent(node2):
        continue
    union(node1, node2)
    edge_cnt += 1
    answer += dist

print(answer)


