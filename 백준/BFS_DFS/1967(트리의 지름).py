import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

leaf = []
visit = [False] * (N+1)


def dfs(node, distance):
    visit[node] = True
    end = True

    for x in tree[node]:
        if not visit[x[0]]:
            end = False
            dfs(x[0], distance + x[1])

    if end:
        leaf.append((node, distance))


dfs(1, 0)
leaf.sort(key=lambda x : x[1])
point1 = leaf[-1]

leaf.clear()
for i in range(len(visit)):
    visit[i] = False

dfs(point1[0], 0)
leaf.sort(key=lambda x:x[1])

point2 = leaf[-1]

print(point2[1])
