import sys
V = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
visit1 = [False] * (V+1)
visit2 = [False] * (V+1)
farthestNode = [0, 0]

for _ in range(V):
    info = list(map(int, sys.stdin.readline().split()))

    i = 1
    pair = [0, 0]
    while i < len(info):
        if i % 2 == 1:
            pair[0] = info[i]
        if i % 2 == 0:
            pair[1] = info[i]
            graph[info[0]].append((pair[0], pair[1]))
            pair = [0, 0]
        i += 1


def dfs(node, dist, visit):
    global farthestNode

    visit[node] = True
    if farthestNode[1] < dist:
        farthestNode = [node, dist]

    for node, d in graph[node]:
        if not visit[node]:
            dfs(node, dist + d, visit)


dfs(1, 0, visit1)
dfs(farthestNode[0], 0, visit2)
print(farthestNode[1])
