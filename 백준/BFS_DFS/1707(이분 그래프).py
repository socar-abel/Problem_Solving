import sys

sys.setrecursionlimit(10 ** 6)

K = int(sys.stdin.readline())


def dfs(graph, visit, node, color):
    visit[node] = color

    for x in graph[node]:
        if visit[x] == 'None':
            if color == 'Red':
                dfs(graph, visit, x, 'Blue')
            elif color == 'Blue':
                dfs(graph, visit, x, 'Red')


while K > 0:
    V, E = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(V + 1)]
    visit = ['None'] * (V+1)

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for x in range(1, V + 1):
        if visit[x] == 'None':
            dfs(graph, visit, x, 'Red')

    check = True

    for node in range(1, V+1):
        for x in graph[node]:
            if visit[node] == visit[x]:
                check = False
                break

    if check:
        print('YES')
    else:
        print('NO')

    K -= 1
